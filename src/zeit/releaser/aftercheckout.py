import os.path
import shutil
import tomli
import zest.releaser.utils


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
    config = os.path.join(workingdir, 'pyproject.toml')
    if not os.path.exists(config):
        return None
    with open(config, 'rb') as f:
        config = tomli.load(f)
    section = 'zeit-releaser'
    key = 'directory'
    if section not in config.get('tool', {}):
        return None
    section = config['tool'][section]
    return section.get(key)
