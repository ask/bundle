from yolk.pypi import CheeseShop as PyPI

from .utils import say


class Version(list):
    develindex = None
    _pypi = None

    def __init__(self, package_name, value):
        self.package_name = package_name
        value, _, self.devel = value.partition('-')
        list.__init__(self, map(int, value.split(".")))

    def __str__(self):
        return ".".join(map(str, self)) + self._develpart

    def __repr__(self):
        return str(self)

    def bump(self):
        if self.is_devel:
            raise ValueError("Can't bump development versions")
        if len(self) < 3:
            self.append(0)
        self[-1] += 1
        return self

    def bump_if_released(self):
        while 1:
            if not self.is_released:
                break
            self.bump()
            say("Version taken: trying next version %s" % (self, ))
        return str(self)

    def sync_with_released_version(self):
        prev = str(self)
        while 1:
            if not self.is_released:
                return prev
            prev = str(self)
            self.bump()

    @property
    def is_released(self):
        return bool(self.pypi.release_urls(self.package_name, str(self)))

    @property
    def is_devel(self):
        return bool(self.devel)

    @property
    def _develpart(self):
        if self.devel:
            return '-' + self.devel
        return ''

    @property
    def pypi(self):
        if self._pypi is None:
            self._pypi = PyPI()
        return self._pypi
