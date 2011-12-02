from . import Bundle


class Dist(object):
    base_fmt = "%(name)s>=%(series)s,<%(next_major)s.0"

    def __init__(self, name, version_tuple, **defaults):
        self.name = name
        self.version_tuple = version_tuple
        self.series = "%s.%s" % self.version_tuple[:2]
        self.next_major = self.version_tuple[0] + 1
        self.as_requirement = \
                self.base_fmt % {"name": self.name,
                                 "series": self.series,
                                 "next_major": self.next_major}
        self.defaults = defaults
        self.defaults.setdefault("version", self.series)

    def __str__(self):
        return self.as_requirement

    def ext(self, *deps):
        return [str(self)] + list(map(str, deps))

    def Bundle(self, name, description, requires, **kwargs):
        return Bundle(name, description, self.ext(*requires),
                    **dict(self.defaults, **kwargs))
