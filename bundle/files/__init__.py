from __future__ import absolute_import
from __future__ import with_statement

import os


def get(*path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *path)


def open(filename, mode='r'):
    return file(get(filename), mode)


def slurp(filename):
    with open(filename) as f:
        return f.read()
