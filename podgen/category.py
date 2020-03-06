# -*- coding: utf-8 -*-
"""
    podgen.category
    ~~~~~~~~~~~~~~~

    This module contains Category, which represents a single iTunes category.

    :copyright: 2016, Thorben Dahl <thorben@sjostrom.no>
    :license: FreeBSD and LGPL, see license.* for more details.
"""
# Support for Python 2.7
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import warnings
from podgen.warnings import LegacyCategoryWarning


class Category(object):
    """Immutable class representing an Apple Podcasts category.

    By using this class, you can be sure that the chosen category is a
    valid category, that it is formatted correctly and you will be warned
    when using an old category.

    See https://help.apple.com/itc/podcasts_connect/#/itc9267a2f12 for an
    overview of the available categories and their subcategories.

    .. versionchanged:: 1.1.0
       Updated to reflect `the new categories <https://podnews.net/article/apple-changed-podcast-categories-2019>`_
       as of August 9th 2019 and yield a
       :class:`~podgen.warnings.LegacyCategoryWarning` when using one of the
       old categories.

    .. note::

        The categories are case-insensitive, and you may escape ampersands.
        The category and subcategory will end up properly capitalized and
        with unescaped ampersands.

    Example::

        >>> from podgen import Category
        >>> c = Category("Music")
        >>> c.category
        Music
        >>> c.subcategory
        None
        >>>
        >>> d = Category("games &amp; hobbies", "Video games")
        >>> d.category
        Games & Hobbies
        >>> d.subcategory
        Video Games
    """

    _legacy_categories = {
        'Arts': ['Design', 'Fashion & Beauty', 'Food', 'Literature',
                 'Performing Arts', 'Visual Arts'],
        'Business': ['Business News', 'Careers', 'Investing',
                     'Management & Marketing', 'Shopping'],
        'Comedy': [],
        'Education': ['Education', 'Education Technology',
                      'Higher Education', 'K-12', 'Language Courses', 'Training'],
        'Games & Hobbies': ['Automotive', 'Aviation', 'Hobbies',
                            'Other Games', 'Video Games'],
        'Government & Organizations': ['Local', 'National', 'Non-Profit',
                                       'Regional'],
        'Health': ['Alternative Health', 'Fitness & Nutrition', 'Self-Help',
                   'Sexuality'],
        'Kids & Family': [],
        'Music': [],
        'News & Politics': [],
        'Religion & Spirituality': ['Buddhism', 'Christianity', 'Hinduism',
                                    'Islam', 'Judaism', 'Other', 'Spirituality'],
        'Science & Medicine': ['Medicine', 'Natural Sciences',
                               'Social Sciences'],
        'Society & Culture': ['History', 'Personal Journals', 'Philosophy',
                              'Places & Travel'],
        'Sports & Recreation': ['Amateur', 'College & High School',
                                'Outdoor', 'Professional'],
        'Technology': ['Gadgets', 'Tech News', 'Podcasting',
                       'Software How-To'],
        'TV & Film': []
    }

    _categories = {
        'Arts': [
            'Books',
            'Design',
            'Fashion & Beauty',
            'Food',
            'Performing Arts',
            'Visual Arts',
        ],
        'Business': [
            'Careers',
            'Entrepreneurship',
            'Investing',
            'Management',
            'Marketing',
            'Non-Profit',
        ],
        'Comedy': [
            'Comedy Interviews',
            'Improv',
            'Stand-up',
        ],
        'Education': [
            'Courses',
            'How To',
            'Language Learning',
            'Self-Improvement',
        ],
        'Fiction': [
            'Comedy Fiction',
            'Drama',
            'Science Fiction',
        ],
        'Government': [],
        'History': [],
        'Health & Fitness': [
            'Alternative Health',
            'Fitness',
            'Medicine',
            'Mental Health',
            'Nutrition',
            'Sexuality',
        ],
        'Kids & Family': [
            'Education for Kids',
            'Parenting',
            'Pets & Animals',
            'Stories for Kids',
        ],
        'Leisure': [
            'Animation & Manga',
            'Automotive',
            'Aviation',
            'Crafts',
            'Games',
            'Hobbies',
            'Home & Garden',
            'Video Games',
        ],
        'Music': [
            'Music Commentary',
            'Music History',
            'Music Interviews',
        ],
        'News': [
            'Business News',
            'Daily News',
            'Entertainment News',
            'News Commentary',
            'Politics',
            'Sports News',
            'Tech News',
        ],
        'Religion & Spirituality': [
            'Buddhism',
            'Christianity',
            'Hinduism',
            'Islam',
            'Judaism',
            'Religion',
            'Spirituality',
        ],
        'Science': [
            'Astronomy',
            'Chemistry',
            'Earth Sciences',
            'Life Sciences',
            'Mathematics',
            'Natural Sciences',
            'Nature',
            'Physics',
            'Social Sciences',
        ],
        'Society & Culture': [
            'Documentary',
            'Personal Journals',
            'Philosophy',
            'Places & Travel',
            'Relationships',
        ],
        'Sports': [
            'Baseball',
            'Basketball',
            'Cricket',
            'Fantasy Sports',
            'Football',
            'Golf',
            'Hockey',
            'Rugby',
            'Running',
            'Soccer',
            'Swimming',
            'Tennis',
            'Volleyball',
            'Wilderness',
            'Wrestling',
        ],
        'Technology': [],
        'True Crime': [],
        'TV & Film': [
            'After Shows',
            'Film History',
            'Film Interviews',
            'Film Reviews',
            'TV Reviews',
        ],
    }

    def __init__(self, category, subcategory=None):
        """Create new Category object. See the class description of
        :class:´~podgen.category.Category`.

        :param category: Category of the podcast.
        :type category: str
        :param subcategory: (Optional) Subcategory of the podcast.
        :type subcategory: str or None
        """
        if not category:
            raise TypeError("category must be provided, was \"%s\"" % category)
        try:
            canonical_category, canonical_subcategory = self._look_up_category(
                category,
                subcategory,
                self._categories,
            )
        except ValueError:
            # Maybe this is a legacy category?
            canonical_category, canonical_subcategory = self._look_up_category(
                category,
                subcategory,
                self._legacy_categories,
            )
            # Okay, it is, warn about this
            warnings.warn(
                'The category ("%s", "%s") is a legacy category. Please switch '
                'to one of the new Apple Podcast categories.' %
                (canonical_category, canonical_subcategory),
                category=LegacyCategoryWarning,
                stacklevel=2
            )

        self.__category = canonical_category
        self.__subcategory = canonical_subcategory

    def _look_up_category(
            self,
            category,
            subcategory,
            available_categories
    ):
        # Do a case-insensitive search for the category
        search_category = category.strip().replace("&amp;", "&").lower()
        for actual_category in available_categories:
            if actual_category.lower() == search_category:
                # We found it
                canonical_category = actual_category
                break
        else:  # no break
            raise ValueError('Invalid category "%s"' % category)

        # Do a case-insensitive search for the subcategory, if provided
        canonical_subcategory = None
        if subcategory is not None:
            search_subcategory = subcategory.strip().replace("&amp;", "&")\
                .lower()
            for actual_subcategory in available_categories[canonical_category]:
                if actual_subcategory.lower() == search_subcategory:
                    canonical_subcategory = actual_subcategory
                    break
            else:  # no break
                raise ValueError('Invalid subcategory "%s" under category "%s"'
                                 % (subcategory, canonical_category))

        return canonical_category, canonical_subcategory

    @property
    def category(self):
        """The category represented by this object. Read-only.

        :type: :obj:`str`
        """
        return self.__category
        # Make this attribute read-only by not implementing setter

    @property
    def subcategory(self):
        """The subcategory this object represents. Read-only.

        :type: :obj:`str`
        """
        return self.__subcategory
        # Make this attribute read-only by not implementing setter

    def __repr__(self):
        return 'Category(category=%s, subcategory=%s)' % \
               (self.category, self.subcategory)
