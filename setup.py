from setuptools import setup, find_packages

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='zeit.releaser',
    version='0.9.0.dev0',
    long_description=long_description,
    author=u'Ron Drongowski',
    author_email='ron.drongowski@zeit.de',
    install_requires=[
          'setuptools',
          'tomli',
          'zest.releaser>=3.12',
      ],
    entry_points={
        'zest.releaser.releaser.after_checkout': [
                'action = zeit.releaser.aftercheckout:copy_unstaged_sources',
        ],
    },
    extras_require={
       'test': [
            'mock',
            'pytest',
        ],
    },
    namespace_packages=['zeit', 'zeit.releaser'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
)
