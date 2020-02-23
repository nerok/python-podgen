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

from podgen import Chapter


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

    def do_attribute_test(self):
        assert self.c.start == self.start
        assert self.c.title == self.title
        assert self.c.link == self.link
        assert self.c.image == self.image

    def test_startIsTimedelta(self):
        self.assertRaises(ValueError, Chapter, "start", self.title)
        self.assertRaises(ValueError, Chapter, 45.0, self.title)
        self.do_attribute_test()

    def test_isImmutable(self):
        self.assertRaises(AttributeError, setattr, self.c, "start", self.start + timedelta(minutes=1))
        self.do_attribute_test()

        self.assertRaises(AttributeError, setattr, self.c, "title", self.title + " here")
        self.do_attribute_test()

        self.assertRaises(AttributeError, setattr, self.c, "link", self.link + "/about")
        self.do_attribute_test()

        self.assertRaises(AttributeError, setattr, self.c, "image", self.image + "/real_image.png")
        self.do_attribute_test()
