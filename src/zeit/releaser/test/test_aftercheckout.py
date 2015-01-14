import zeit.releaser.aftercheckout
import zest.releaser.utils
from mock import Mock
from mock import patch


def test_copy_unstaged_src_should_only_be_processed_for_frontend(monkeypatch):
    def ask(q):
        return True
    data = {}
    data['name'] = 'something'
    monkeypatch.setattr(zest.releaser.utils, 'ask', ask)
    assert zeit.releaser.aftercheckout.copy_unstaged_sources(data) is None


def test_copy_unstaged_src_should_be_processed_for_frontend(monkeypatch):
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

    with patch.object(zeit.releaser.aftercheckout, 'copy_js_css') as mock_method:
        mock_method.return_value = None
        zeit.releaser.aftercheckout.copy_unstaged_sources(data)

    mock_method.assert_called_once_with('workingdir', 'tagdir')
