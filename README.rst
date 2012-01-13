===================================
 Create and manage bundle packages
===================================

:Version: 1.1.2

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


As a setuptools plugin
----------------------

If you use bundles for extension dependencies then you can use ``setup.py``
to manage them.

If you have a library called ``george``, with bundles defined in ``george.bundles``
like this::

    from bundle.extensions import Dist

    # version must be a tuple of at least 2 elements,
    # e.g. (1, 2), or (1, 2, 6).
    from george import VERSION

    defaults = {"author": "George Costanza",
                "author_email": "art@vandelay.com",
                "url": "http://vandelay.com",
                "license": "BSD"}
    george = Dist("george", VERSION, **defaults)

    bundles = [
        george.Bundle("george-with-django",
                      "Bundle installing george and Django",
                      requires=['django>=1.2']),
        george.Bundle("george-in-production",
                      "Bundle for george and deps suitable for production",
                      requires=["celery", "psycopg2", "ultrajson"]),
    ]


With your bundles list you can now tell ``setup.py`` where to find it,
by adding it to the ``bundle.bundles`` entrypoints.

In george's ``setup.py`` add::

    setup(
        ...
        entry_points = {
            "bundle.bundles": ["george = george.bundles:bundles"]
        },
    )

And then you can manage your bundles with the ``register_bundles``,
``upload_bundles``, and ``upload_bundles_fix`` setup commands::

    $ python setup.py upload_bundles

Note that you need run ``setup.py develop`` or ``setup.py install``
first, so that the entry points are properly installed before you
run bundle commands.  And you need to have your PyPI credentials
properly setup in your `~/.pypirc` file.

The commands are:

:upload_bundles:
    Uploads bundles to PyPI, but only the bundles for which version
    has not been uploaded before.

:register_bundles:
    Register the bundles at PyPI.  ``upload_bundles`` will also
    register, but this is useful if you only need to change metadata
    without uploading a new version.

:upload_bundles_fix:
    Bumps the last version number for all of the bundles
    and uploads the bundles to PyPI.

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
