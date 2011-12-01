===================================
 Create and manage bundle packages
===================================

:Version: 1.0.0

Synopsis
========

A bundle consists of several packages, and can be used as a shortcut in
applications and libraries requirements lists.

Bundles are used to follow a
common group of packages, or a package with an optional extension feature.

This distribution lets you create bundles, and may also be able to manage
installed bundles in the future.

Usage
=====

You can create and upload a bundle to PyPI::

    >>> b = Bundle("mybundle", description="Cool bundle",
                  version="1.0.0",
                  requires=["pkg1", "pkg2>1.3", "pkg3"],
                  author="George Costanza",
                  author_email="george@vandelay.com",
                  url="http://vandelay.com",
                  license="BSD")
    >>> b.upload()

Note that this requires a ``.pypirc`` containing your PyPI login information.


Installation
============

You can install `Bundle` either via the Python Package Index (PyPI)
or from source.

To install using `pip`,::

    $ pip install bundle

To install using `easy_install`,::

    $ easy_install bundle

If you have downloaded a source tarball you can install it
by doing the following,::

    $ python setup.py build
    # python setup.py install # as root

Getting Help
============

Bug tracker
===========

If you have any suggestions, bug reports or annoyances please report them
to our issue tracker at http://github.com/ask/bundle/issues/

Contributing
============

Development of `Bundle` happens at Github: http://github.com/ask/bundle

You are highly encouraged to participate in the development. If you don't
like Github (for some reason) you're welcome to send regular patches.

License
=======

This software is licensed under the `New BSD License`. See the `LICENSE`
file in the top distribution directory for the full license text.
