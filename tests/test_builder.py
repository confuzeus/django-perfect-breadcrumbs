import unittest

from django_perfect_breadcrumbs.builder import Breadcrumb, BreadcrumbBuilder


class BuilderTests(unittest.TestCase):
    def test_default_breadcrumbs_is_empty_list(self):
        builder = BreadcrumbBuilder()
        self.assertIsInstance(builder.breadcrumbs, list)
        self.assertEqual(len(builder.breadcrumbs), 0)

    def test_non_list_initial_raises_exception(self):
        with self.assertRaises(ValueError):
            BreadcrumbBuilder(initial=1)

    def test_set_non_breadcrumb_initial_list_item_raises_exception(self):
        with self.assertRaises(ValueError):
            BreadcrumbBuilder(initial=[1])

    def test_initial_breadcrumbs_are_set(self):
        builder = BreadcrumbBuilder(initial=[Breadcrumb("Test", "/test")])
        self.assertEqual(len(builder.breadcrumbs), 1)

    def test_active_breadcrumb_with_url_raises_exception(self):
        with self.assertRaises(ValueError):
            Breadcrumb("test", "/test", True)

    def test_non_active_breadcrumb_without_url_raises_exception(self):
        with self.assertRaises(ValueError):
            Breadcrumb(
                "Test",
            )

    def test_item_added(self):
        builder = BreadcrumbBuilder()
        self.assertEqual(len(builder.breadcrumbs), 0)
        builder.add("Test", "/test")
        self.assertEqual(len(builder.breadcrumbs), 1)

    def test_breadcrumb_item_added(self):
        builder = BreadcrumbBuilder()
        self.assertEqual(len(builder.breadcrumbs), 0)
        builder.add_breadcrumb(Breadcrumb("Test", "/test"))
        self.assertEqual(len(builder.breadcrumbs), 1)

    def test_add_bulk_with_non_list_breadcrumbs(self):
        builder = BreadcrumbBuilder()
        with self.assertRaises(ValueError):
            builder.add_bulk(1)

    def test_add_bulk_dicts(self):
        builder = BreadcrumbBuilder()
        self.assertEqual(len(builder.breadcrumbs), 0)
        breadcrumbs = []
        for _ in range(3):
            breadcrumbs.append({"name": "Test", "url": "/test"})
        builder.add_bulk(breadcrumbs)
        self.assertEqual(len(builder.breadcrumbs), 3)

    def test_add_bulk_breadcrumbs(self):
        builder = BreadcrumbBuilder()
        self.assertEqual(len(builder.breadcrumbs), 0)
        breadcrumbs = []
        for _ in range(3):
            breadcrumbs.append(Breadcrumb("Test", "/test"))
        builder.add_bulk(breadcrumbs)
        self.assertEqual(len(builder.breadcrumbs), 3)
