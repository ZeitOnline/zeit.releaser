import ConfigParser
import os.path
import shutil
import zest.releaser.utils


def copy_unstaged_sources(data):
    target = select_target(data['name'])
    if not target:
        return
    if not zest.releaser.utils.ask('Copy js and css to tag-checkout'):
        return
    copy_js_css(data['workingdir'], data['tagdir'], target)


def copy_js_css(src, dest, target):
    print 'deleting %s/%s' % (dest, target)
    shutil.rmtree('%s/%s' % (dest, target))
    print 'copying %s/%s to %s/%s' % (src, target, dest, target)
    shutil.copytree('%s/%s' % (src, target), '%s/%s' % (dest, target))


def select_target(package):
    config = read_configuration('~/.pypirc')
    section = 'zeit.releaser'
    if section not in config.sections():
        if package == 'zeit.web':
            return 'src/zeit/web/static'
        else:
            return None
    elif not config.has_option(section, package):
        return None
    else:
        return config.get(section, package)


def read_configuration(filename):
    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser(filename))
    return config
