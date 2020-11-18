import os.path
import shutil
import sys
import zest.releaser.utils

if sys.version_info < (3,):
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser


def copy_unstaged_sources(data):
    target = select_target(data['workingdir'])
    if not target:
        return
    if not zest.releaser.utils.ask('Copy js and css to tag-checkout'):
        return
    copy_js_css(data['workingdir'], data['tagdir'], target)


def copy_js_css(src, dest, target):
    if os.path.exists(target):
        print('deleting %s/%s' % (dest, target))
        shutil.rmtree('%s/%s' % (dest, target))
    print('copying %s/%s to %s/%s' % (src, target, dest, target))
    shutil.copytree('%s/%s' % (src, target), '%s/%s' % (dest, target))


def select_target(workingdir):
    config = read_configuration(os.path.join(workingdir, 'setup.cfg'))
    section = 'zeit.releaser'
    key = 'directory'
    if section not in config.sections():
        return None
    elif not config.has_option(section, key):
        return None
    else:
        return config.get(section, key)


def read_configuration(filename):
    config = ConfigParser()
    config.read(os.path.expanduser(filename))
    return config
