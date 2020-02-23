# -*- coding: utf-8 -*-
"""
    podgen.tests.test_util
    ~~~~~~~~~~~~~~~~~~~~~~

    Test some of the functions found in the util module.

    :copyright: 2016, Thorben Dahl <thorben@sjostrom.no>
    :license: FreeBSD and LGPL, see license.* for more details.
"""
# Support for Python 2.7
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import unittest
from datetime import timedelta
from ddt import ddt, data, unpack
from podgen import util


@ddt
class TestUtil(unittest.TestCase):

    @data(
        ([], "(empty)"),
        ([4], "4"),
        ([4, "hi"], "4 and hi"),
        ([4, "hi", "low"], "4, hi and low")
    )
    @unpack
    def test_listToHumanReadableStr(self, test_list, expected):
        actual = util.listToHumanreadableStr(test_list)
        self.assertEqual(actual, expected)

    @data(
        (None, None),
        (timedelta(seconds=4), "00:04"),
        (timedelta(minutes=4), "04:00"),
        (timedelta(hours=4), "04:00:00"),
        (timedelta(days=2, hours=3, minutes=41, seconds=51), "51:41:51"),
        (timedelta(days=2, hours=3, minutes=4, seconds=5), "51:04:05"),
        (timedelta(seconds=4, milliseconds=42), "00:04.042")
    )
    @unpack
    def test_ntpFormatWithMillis(self, td, expected):
        actual = util.format_as_normal_play_time(td)
        self.assertEqual(actual, expected)

    def test_ntpFormatWithoutMillis(self):
        td = timedelta(seconds=4, milliseconds=42)
        actual = util.format_as_normal_play_time(td, False)
        self.assertEqual(actual, "00:04")

