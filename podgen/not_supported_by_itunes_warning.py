# -*- coding: utf-8 -*-
"""
    podgen.not_supported_by_itunes_warning
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This file contains the NotSupportedByItunesWarning, which is used when the
    library is used in a way that is not compatible with iTunes.

    :copyright: 2016, Thorben Dahl <thorben@sjostrom.no>
    :license: FreeBSD and LGPL, see license.* for more details.
"""
# Support for Python 2.7
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *


class NotSupportedByItunesWarning(UserWarning):
    pass
