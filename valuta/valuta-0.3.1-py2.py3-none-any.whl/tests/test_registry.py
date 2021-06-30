import unittest

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestRegistry",)


class TestRegistry(unittest.TestCase):
    """Test registry."""

    def test_import_from_registry(self):
        """Test import from deprecated `valuta.registry` module."""
        from ..registry import Registry
