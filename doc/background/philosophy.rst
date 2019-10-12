----------
Philosophy
----------

This project is heavily inspired by the "for humans" approach of the
`Requests <https://requests.readthedocs.io>`__ library, which features an API that
is designed to give the developer a great user experience. This is done by
finding a suitable scope and abstraction level, and designing the
API so it supports the developer's vocabulary and their mental model of how
the domain works.

For example, instead of using the names of XML tags like "itunes:image", a more
relevant name, here simply "image", is used. Another example is the duration of
a podcast episode. In XML terms, this is put into an "itunes:duration" tag which exists
outside of the "enclosure" tag, which holds the filename and file size. In PodGen,
the filename, file size, file type and audio duration are all placed together in
a Media instance, since they are all related to the media itself. The goal
has been to "hide" the messy details of the XML and provide an API on top which
uses words that you recognize and use daily when working with podcasts.

To be specific, PodGen aims to follow the same
`PEP 20 <https://www.python.org/dev/peps/pep-0020/>`__ idioms as
`Requests <https://requests.readthedocs.io/en/master/user/intro/#philosophy>`__:

1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Readability counts.

To enable this, the project focuses on one task alone: making it easy to generate a podcast.
