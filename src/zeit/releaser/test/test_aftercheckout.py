from mock import Mock
from mock import patch
import os.path
import pytest
import zeit.releaser.aftercheckout
import zest.releaser.utils


@pytest.fixture
def pypirc(monkeypatch, tmpdir):
    def expanduser(path):
        return path.replace('~', str(tmpdir))
    monkeypatch.setattr(os.path, 'expanduser', expanduser)
    return str(tmpdir / '.pypirc')


def test_copy_unstaged_src_should_only_be_processed_for_configured_packages(
        monkeypatch, pypirc):
    def ask(q):
        return True
    monkeypatch.setattr(zest.releaser.utils, 'ask', ask)

    data = {}
    data['name'] = 'something'
    data['workingdir'] = 'workingdir'
    data['tagdir'] = 'tagdir'
    assert zeit.releaser.aftercheckout.copy_unstaged_sources(data) is None

    with open(pypirc, 'w') as f:
        f.write("""\
[zeit.releaser]
something = foo""")

    with patch.object(zeit.releaser.aftercheckout, 'copy_js_css') as copy:
        zeit.releaser.aftercheckout.copy_unstaged_sources(data)
        copy.assert_called_once_with(
            'workingdir', 'tagdir', 'foo')


def test_copy_unstaged_src_should_be_processed_for_frontend(
        monkeypatch, pypirc):
    def ask(q):
        return True
    monkeypatch.setattr(zest.releaser.utils, 'ask', ask)

    copy_js_css = Mock(return_value='True')
    monkeypatch.setattr(
        zeit.releaser.aftercheckout, 'copy_js_css', copy_js_css)

    data = {}
    data['name'] = 'zeit.web'
    data['workingdir'] = 'workingdir'
    data['tagdir'] = 'tagdir'

    with patch.object(zeit.releaser.aftercheckout, 'copy_js_css') as copy:
        copy.return_value = None
        zeit.releaser.aftercheckout.copy_unstaged_sources(data)

    copy.assert_called_once_with('workingdir', 'tagdir', 'src/zeit/web/static')
