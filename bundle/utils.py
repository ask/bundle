import string
import os
import sys

from contextlib import contextmanager
from shutil import rmtree
from tempfile import mkdtemp
from textwrap import TextWrapper

plain = frozenset("-.=" + string.letters + string.digits)


def say(m):
    sys.stderr.write("%s\n" % (m, ))


def quote(text, ws=plain):
    """Quote special characters in shell command arguments.

    E.g ``--foo bar>=10.1`` becomes "--foo bar\>\=10\.1``.

    """
    return "".join(chr in ws and chr or '\\' + chr
                        for chr in text)


def indent(s, n=4):
    return "\n".join(' ' * n + line for line in s.split('\n'))


def codewrap(s, w=50, i=4):
    wrapper = TextWrapper(width=50, break_on_hyphens=False)
    lines = wrapper.wrap(s)
    return "\n".join([lines[0]] + [indent(l, i)
                                    for l in lines[1:]])


def maybe_opt(opt, value):
    if value is not None:
        if opt.endswith('='):
            return ["%s='%s'" % (opt[:-1], str(value))]
        return [opt, str(value)]
    return []


def maybe_flag(flag, value):
    if value is not None:
        return [flag]
    return []


@contextmanager
def changedir(new):
    prev = os.getcwd()
    os.chdir(new)
    yield new
    os.chdir(prev)


@contextmanager
def tempdir():
    dirname = mkdtemp()
    yield dirname
    rmtree(dirname)
