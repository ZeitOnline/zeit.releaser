zeit.releaser
-------------

This is a plugin for zest.releaser and is for zeit.web mainly.
We want to release js and css which is not part of the repo. So we
need to check it after a clean checkout.

To configure the applicable packages, add a section to your ~/.pypirc like the
following::

    [zeit.releaser]
    package.one = src/package/one/static
    package.two = src/package/two/resources

(For backwards-compatibility reasons, the assumed default entry if nothing is
configured is ``zeit.web = src/zeit/web/static``.)
