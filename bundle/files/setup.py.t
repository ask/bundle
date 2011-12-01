#!/usr/bin/env python
import os
import codecs

from setuptools import setup

if os.path.exists("README"):
    long_description = codecs.open("README", "r", "utf-8").read()
else:
    long_description = '''\
This is a bundle of several packages that you can use as a shortcut in the
requirements lists of your applications.  Bundles are used to follow a
common group of packages, or a package with an optional extension feature.
'''

setup(name='$name',
      version='$version',
      description='''$description''',
      author='''$author''',
      author_email='$author_email',
      url='''$url''',
      platforms=$platforms,
      license='''$license''',
      zip_safe=False,
      install_requires=$requires_i24,
      classifiers=[
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      long_description=long_description,
)
