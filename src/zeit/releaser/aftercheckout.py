#!/usr/bin/python
# -*- coding: utf-8 -*-

import zest.releaser.utils
import shutil

target = 'src/zeit/web/static'


def copy_unstaged_sources(data):
    if not data['name'] == 'zeit.web':
        return
    if not zest.releaser.utils.ask('Copy js and css to tag-checkout'):
        return
    copy_js_css(data['workingdir'], data['tagdir'])


def copy_js_css(src, dest):
    print 'deleting %s/%s' % (dest, target)
    shutil.rmtree('%s/%s' % (dest, target))
    print 'copying %s/%s to %s/%s' % (src, target, dest, target)
    shutil.copytree('%s/%s' % (src, target), '%s/%s' % (dest, target))
