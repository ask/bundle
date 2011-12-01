$title_h1
$title
$title_h1

:Version: $version

Contents
========

This bundle installs the following packages::

    $requires_i2

What is this?
=============

This is a bundle of several packages that you can use as a shortcut in the
requirements lists of your applications.  Bundles are used to follow a
common group of packages, or a package with an optional extension feature.

You can install all of the packages in this bundle by,

*using pip*::

    $$ pip install -U $name

or *using easy_install*::

    $$ easy_install -U $name

Or if you want to add this bundle as a dependency in your application, you
can add the following identifier in your ``setup.py``'s requires list or
in your pip requirements files::

    $name

You can also specify a specific version::

    $name>=$version
