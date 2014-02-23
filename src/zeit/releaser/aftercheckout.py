#!/usr/bin/python
# -*- coding: utf-8 -*-

import zest.releaser.utils
import shutil

target = 'src/zeit/frontend'


def copy_unstaged_sources(data):
    if not data['name'] == 'zeit.frontend':
        return
    if not zest.releaser.utils.ask('Copy js and css to tag-checkout'):
        return
    copy_js_css(data['workingdir'], data['tagdir'])


def copy_js_css(src, dest):
    print 'copying %s/%s/css to %s/%s' % (src, target, dest, target)
    shutil.copytree('%s/%s/css' % (src, target), '%s/%s/css' % (dest, target))

    print 'copying %s/%s/js to %s/%s' % (src, target, dest, target)
    shutil.copytree('%s/%s/js' % (src, target), '%s/%s/js' % (dest, target))
