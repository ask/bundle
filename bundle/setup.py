from __future__ import absolute_import

from distutils import log
from distutils.command.upload import upload as _upload
from pkg_resources import iter_entry_points


class BundleCommand(_upload):

    user_options = _upload.user_options + [
        # - from 'register'
        ("strict", None,
         "Will stop if the meta-data are not fully compliant"),

        # - from 'sdist'
        ("formats=", None,
         "formats for source distribution (comma-separated list)"),
    ]
    boolean_options = _upload.boolean_options + ["strict"]
    _bundles = None

    def handle(self):
        for bundle in self.get_bundles():
            self.handle_bundle(bundle)

    def handle_bundle(self, bundle):
        raise NotImplementedError("subclass responsibility")

    def run(self):
        if not self.username:
            raise KeyError(
                    "Missing PyPI username:  Do you have a valid .pypirc?")
        if not self.get_bundles():
            return log.error("No bundle entry-points for distribution %r" % (
                self.distribution.metadata.name, ))
        self.handle()

    def get_bundles(self):
        # can't use property because of ancient old-style classes used.
        if not self._bundles:
            self._bundles = self._get_bundles()
        return self._bundles

    def _get_bundles(self):
        for ep in iter_entry_points('bundle.bundles'):
            if ep.name == self.distribution.metadata.name:
                return ep.load()


class register_bundles(BundleCommand):
    description = "Register bundles at PyPI"

    def handle_bundle(self, bundle):
        log.info("* Registering bundle %s (%s)" % (bundle.name,
                                                   bundle.version))
        bundle.register()


class upload_bundles(BundleCommand):
    description = "Upload bundles to PyPI (if version not already released)"

    def handle_bundle(self, bundle):
        log.info("* Uploading bundle %s (%s)" % (bundle.name,
                                                 bundle.version))
        bundle.upload()


class upload_bundles_fix(BundleCommand):
    description = "Uploads new version of all bundles to PyPI"

    def handle_bundle(self, bundle):
        log.info("* Uploading new bundle version for %s (%s)" % (
            bundle.name, bundle.version))
        bundle.upload_fix()
