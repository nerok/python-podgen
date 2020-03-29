# -*- coding: utf-8 -*-
"""
    podgen.tests.test_chapter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Module for testing the Chapter class.

    :copyright: 2020, Thorben Dahl <thorben@sjostrom.no>
    :license: FreeBSD and LGPL, see license.* for more details.
"""
# Support for Python 2.7
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import unittest
from datetime import timedelta
import warnings
import sys

from ddt import ddt, data

from podgen import Chapter
from podgen.warnings import NotRecommendedWarning
from podgen.util import EncapsulatedStr


@ddt
class TestChapter(unittest.TestCase):
    def setUp(self):
        self.start = timedelta(seconds=15)
        self.title = "Welcome"
        self.link = "https://example.com"
        self.image = "https://example.com/image.png"

        self.c = Chapter(
            self.start,
            self.title,
            self.link,
            self.image
        )

        # Ensure warning capturing works (only needed for Python 2.7 -- otherwise
        # we could just have used assertWarns)
        for v in sys.modules.values():
            if getattr(v, '__warningregistry__', None):
                v.__warningregistry__ = {}

    def test_constructorPositional(self):
        self.do_attribute_test()

    def test_constructorKeyword(self):
        self.c = Chapter(
            start=self.start,
            title=self.title,
            link=self.link,
            image=self.image
        )
        self.do_attribute_test()

    def test_mandatoryArguments(self):
        self.assertRaises(TypeError, Chapter)
        self.assertRaises(TypeError, Chapter, self.start)

    def test_optionalArguments(self):
        c = Chapter(self.start, self.title)
        assert c.start == self.start
        assert c.title == self.title
        self.assertIsNone(c.link)
        self.assertIsNone(c.image)

    def test_encapsulatedStr(self):
        start = self.start
        title = EncapsulatedStr(self.title)
        link = EncapsulatedStr(self.link)
        image = EncapsulatedStr(self.image)

        c = Chapter(start, title, link, image)

        self.assertEqual(c.start, start)
        self.assertEqual(c.title, title)
        self.assertEqual(c.link, link)
        self.assertEqual(c.image, image)

    def do_attribute_test(self):
        assert self.c.start == self.start
        assert self.c.title == self.title
        assert self.c.link == self.link
        assert self.c.image == self.image

    @data("start", 45.0)
    def test_startIsTimedelta(self, invalid_value):
        self.assertRaises(ValueError, Chapter, invalid_value, self.title)

    @data("", EncapsulatedStr(""), "      ")
    def test_titleIsNotEmpty(self, invalid_value):
        self.assertRaises(ValueError, Chapter, self.start, invalid_value)

    @data("", EncapsulatedStr(""), "ftp://example.org/example.html", "example.org/example.html")
    def test_linkIsValidated(self, invalid_value):
        self.assertRaises(ValueError, Chapter, self.start, self.title, link=invalid_value)

    @data("", EncapsulatedStr(""), "ftp://example.org/example.png", "example.org/example.png")
    def test_imageMustBeHttp(self, invalid_value):
        self.assertRaises(ValueError, Chapter, self.start, self.title, image=invalid_value)

    @data("http://example.org/image.gif", EncapsulatedStr("https://example.org/image"))
    def test_imageShouldHaveAcceptedFileEnding(self, dumb_value):
        # Replacement of assertWarns in Python 2.7
        with warnings.catch_warnings(record=True) as w:
            # Replacement of assertWarns in Python 2.7
            warnings.simplefilter("always", NotRecommendedWarning)

            c = Chapter(self.start, self.title, image=dumb_value)
            self.assertEqual(c.image, dumb_value)

            # Replacement of assertWarns in Python 2.7
            self.assertEqual(len(w), 1)
            self.assertIsInstance(w[0].message, NotRecommendedWarning)

    def test_isImmutable(self):
        self.assertRaises(AttributeError, setattr, self.c, "start", self.start + timedelta(minutes=1))
        self.do_attribute_test()

        self.assertRaises(AttributeError, setattr, self.c, "title", self.title + " here")
        self.do_attribute_test()

        self.assertRaises(AttributeError, setattr, self.c, "link", self.link + "/about")
        self.do_attribute_test()

        self.assertRaises(AttributeError, setattr, self.c, "image", self.image + "/real_image.png")
        self.do_attribute_test()


