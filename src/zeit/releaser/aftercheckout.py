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
    shutil.copytree('%s/%s/css' % (src, target), '%s/%s' % (src, target))
    shutil.copytree('%s/%s/js' % (src, target), '%s/%s' % (src, target))
