# -*- coding: utf-8 -*-
"""
    podgen.tests.test_category
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Module for testing the Category class.

    :copyright: 2016, Thorben Dahl <thorben@sjostrom.no>
    :license: FreeBSD and LGPL, see license.* for more details.
"""
# Support for Python 2.7
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import unittest
import warnings
import sys

from podgen import Category, LegacyCategoryWarning


class TestCategory(unittest.TestCase):
    # Ensure warning capturing works (only needed for Python 2.7 -- otherwise
    # we could just have used assertWarns)
    def setUp(self):
        # The __warningregistry__'s need to be in a pristine state for tests
        # to work properly.
        for v in sys.modules.values():
            if getattr(v, '__warningregistry__', None):
                v.__warningregistry__ = {}

    def test_constructorWithSubcategory(self):
        # Replacement of assertWarns in Python 2.7
        with warnings.catch_warnings(record=True) as w:
            # Replacement of assertWarns in Python 2.7
            warnings.simplefilter("always", LegacyCategoryWarning)

            c = Category("Arts", "Food")
            self.assertEqual(c.category, "Arts")
            self.assertEqual(c.subcategory, "Food")

            # No warning should be given
            # Replacement of assertWarns in Python 2.7
            self.assertEqual(len(w), 0);

    def test_constructorWithoutSubcategory(self):
        c = Category("Arts")
        self.assertEqual(c.category, "Arts")
        self.assertTrue(c.subcategory is None)

    def test_constructorInvalidCategory(self):
        self.assertRaises(ValueError, Category, "Farts", "Food")

    def test_constructorInvalidSubcategory(self):
        self.assertRaises(ValueError, Category, "Arts", "Flood")

    def test_constructorSubcategoryWithoutCategory(self):
        self.assertRaises((ValueError, TypeError), Category, None, "Food")

    def test_constructorCaseInsensitive(self):
        c = Category("arTS", "FOOD")
        self.assertEqual(c.category, "Arts")
        self.assertEqual(c.subcategory, "Food")

    def test_immutable(self):
        c = Category("Arts", "Food")
        self.assertRaises(AttributeError, setattr, c, "category", "Fiction")
        self.assertEqual(c.category, "Arts")

        self.assertRaises(AttributeError, setattr, c, "subcategory", "Science Fiction")
        self.assertEqual(c.subcategory, "Food")

    def test_escapedIsAccepted(self):
        c = Category("Kids &amp; Family", "Pets &amp; Animals")
        self.assertEqual(c.category, "Kids & Family")
        self.assertEqual(c.subcategory, "Pets & Animals")

    def test_oldCategoryIsAcceptedWithWarning(self):
        # Replacement of assertWarns in Python 2.7
        with warnings.catch_warnings(record=True) as w:
            # Replacement of assertWarns in Python 2.7
            warnings.simplefilter("always", LegacyCategoryWarning)

            c = Category("Government & Organizations")
            self.assertEqual(c.category, "Government & Organizations")

            # Replacement of assertWarns in Python 2.7
            self.assertEqual(len(w), 1)
            self.assertIsInstance(w[0].message, LegacyCategoryWarning)

    def test_oldSubcategoryIsAcceptedWithWarnings(self):
        # Replacement of assertWarns in Python 2.7
        with warnings.catch_warnings(record=True) as w:
            # Replacement of assertWarns in Python 2.7
            warnings.simplefilter("always", LegacyCategoryWarning)

            c = Category("Technology", "Podcasting")
            self.assertEqual(c.category, "Technology")
            self.assertEqual(c.subcategory, "Podcasting")

            # Replacement of assertWarns in Python 2.7
            self.assertEqual(len(w), 1)
            self.assertIsInstance(w[0].message, LegacyCategoryWarning)

    def test_oldCategorySubcategoryIsAcceptedWithWarnings(self):
        # Replacement of assertWarns in Python 2.7
        with warnings.catch_warnings(record=True) as w:
            # Replacement of assertWarns in Python 2.7
            warnings.simplefilter("always", LegacyCategoryWarning)

            c = Category("Science & Medicine", "Medicine")
            self.assertEqual(c.category, "Science & Medicine")
            self.assertEqual(c.subcategory, "Medicine")

            # Replacement of assertWarns in Python 2.7
            self.assertEqual(len(w), 1)
            self.assertIsInstance(w[0].message, LegacyCategoryWarning)
