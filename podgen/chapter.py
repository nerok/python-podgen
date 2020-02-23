# -*- coding: utf-8 -*-
"""
    podgen.chapter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Module defining the Chapter class.

    :copyright: 2020, Thorben Dahl <thorben@sjostrom.no>
    :license: FreeBSD and LGPL, see license.* for more details.
"""
# Support for Python 2.7
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

from datetime import timedelta


class Chapter(object):
    """Immutable class representing one chapter in an episode.

    Long episodes may often contain different themes and discussions, some of
    which may not be interesting to everyone. To let users skip a discussion they don't
    find interesting or otherwise navigate inside the episode, you can define
    chapters. One chapter corresponds to one discussion, column or "part" of
    the episode.

    One instance of this class represents one chapter.

    The :attr:`~podgen.Chapter.start` and :attr:`~podgen.Chapter.title`
    attributes are mandatory. An error will be raised when you try to generate
    the podcast RSS if they are not set.

    The attributes that are expected to be :obj:`str` are not converted when
    set. Instead, they are converted when used during the RSS generation.

    Example::

        >>> from podgen import Chapter
        >>> from datetime import timedelta
        >>>
        >>> # Using mandatory arguments only
        >>> c1 = Chapter(timedelta(), "Introduction")
        >>> c2 = Chapter(timedelta(seconds=22), "Welcome")
        >>>
        >>> # Using all available arguments
        >>> c3 = Chapter(
        ...     timedelta(minutes=2, seconds=4),
        ...     "Interview with Podlove",
        ...     "https://podlove.org",
        ...     "https://example.org/images/podlove.png"
        ... )
        >>>
        >>> # Using keyword arguments
        >>> c4 = Chapter(
        ...     title="How to use Podlove Chapters",
        ...     link="https://podlove.org/simple-chapters/"
        ...     start=timedelta(minutes=42, seconds=3),
        ... )
    """

    def __init__(self, start, title, link=None, image=None):
        """Create new Chapter object.

        :param start: The beginning of this chapter, relative to the start of
                      the episode.
        :type start: :obj:`datetime.timedelta`
        :param title: This chapter's title.
        :type title: :obj:`str`
        :param link: The URL of a web page that is related to this chapter.
        :type link: :obj:`str`
        :param image: The URL of an image that should be associated with this
                      chapter.
        :type: image: :obj:`str`
        """
        # Validation
        if not isinstance(start, timedelta):
            raise ValueError("Invalid start. Expected %s to be a datetime.timedelta" % start)

        self.__start = start
        self.__title = title
        self.__link = link
        self.__image = image

    @property
    def start(self):
        """The beginning of this chapter, relative to the start of the episode.

        :type: :class:`datetime.timedelta`
        :RSS: start attribute of psc:chapter
        """
        return self.__start

    @property
    def title(self):
        """This chapter's title.

        Used as label for this chapter.

        :type: :obj:`str`
        :RSS: title attribute of psc:chapter
        """
        return self.__title

    @property
    def link(self):
        """The URL of a web page that is related to this chapter.

        :type: :obj:`str`
        :RSS: href attribute of psc:chapter
        """
        return self.__link

    @property
    def image(self):
        """The URL of an image that should be associated with this chapter.

        :type: :obj:`str`
        :RSS: image attribute of psc:chapter
        """
        return self.__image

    def __repr__(self):
        return "Chapter(start=%r, title=%r, link=%r, image=%r)" % \
               (self.start, self.title, self.link, self.image)
