=============
Why the fork?
=============

This project is a fork of python-feedgen_ which cuts away everything that
doesn't serve the goal of **making it easy and simple to generate podcasts** from
a Python program. Thus, this project includes only a **subset** of the features
of python-feedgen_. And I don't think anyone in their right mind would accept a pull
request which removes 70% of the features ;-) Among other things, support for ATOM and
Dublin Core is removed, and the remaining code is almost entirely rewritten.

A more detailed reasoning follows. Read it if you're interested, but feel free
to skip to the :doc:`/usage_guide/index`.

Inspiration
-----------

The python-feedgen_ project is alright for creating general RSS and ATOM feeds,
especially in situations where you'd like to serve the same content in those two
formats. However, I wanted to create podcasts, and found myself struggling with
getting the library to do what I wanted to do, and I frequently found myself
looking at the source to understand what was going on.

Perhaps the biggest problem is the awkwardness that stems from enabling
RSS and ATOM feeds through the same API. In case you don't know, ATOM is a
competitor to RSS, and has many more capabilities than RSS. However, it is
not used for podcasting. The result of mixing both ATOM and RSS include methods that will map an ATOM value to
its closest sibling in RSS, some in logical ways (like the ATOM method ``rights`` setting
the value of the RSS property ``copyright``) and some differ in subtle ways (like using
(ATOM) ``logo`` versus (RSS) ``image``). Other methods are more complex (see ``link``). They're all
confusing, though, since changing one property automatically changes another implicitly.
They also cause bugs, since it is so difficult to wrap your head around how one
interact with another. This is the inspiration for forking python-feedgen_ and
rewrite the API, without mixing the different standards.

Futhermore, python-feedgen_ gives you a one-to-one
mapping to the resulting XML elements. This means that you must
learn the RSS and podcast standards, which include many legacy elements you
don't really need. For example, the original RSS spec
includes support for an image, but that image is required to be less than 144 pixels
wide (88 pixels being the default) and 400 pixels high (remember, this was year *2000*).
Itunes can't have any of that (understandably so), so they added their own ``itunes:image``
tag, which has its own set of requirements (images can be no smaller than 1400x1400px!).
I believe **the API should help guide the users** by hiding the legacy image tag,
and you as a user shouldn't need to know all this. You just need to know that the
image must be larger than 1400x1400 pixels, not the history behind everything.

Forking a project gives you a lot of freedom, since you don't have to support
any old behaviour. It would be difficult to make these changes upstream, since
many of the problems are inherent to the scope and purpose of the library itself,
and changing that is difficult and not always desirable.


Summary of changes
------------------

If you've used python-feedgen_ and want to move over to PodGen, you might as
well be moving to a completely different library. Everything has been renamed,
some attributes expect :obj:`bool` where they earlier expected :obj:`str`, and
so on – you'll have to forget whatever you've learnt about the library.
Hopefully, the simple API should ease the pain of switching, and make the
resulting code easier to maintain.

The following list is not exhaustive.

* The module is renamed from ``feedgen`` to ``podgen``.
* ``FeedGenerator`` is renamed to :class:`~podgen.Podcast` and ``FeedItem`` is
  renamed to :class:`~podgen.Episode`.
* All classes are available at package level, so you no longer need to import
  them from the module they reside in. For example, :class:`podgen.Podcast` and
  :class:`podgen.Episode`.
* Support for ATOM is removed.
* Stop using getter and setter methods and start using attributes.

  * Compound values (like :attr:`~podgen.Podcast.managing_editor` or
    :attr:`~podgen.Episode.media`) expect
    objects now, like :class:`~podgen.Person` and :class:`~podgen.Media`.

* Remove support for some uncommon, obsolete or difficult to use elements:

  * ttl
  * category
  * image
  * itunes:summary
  * rating
  * textInput

* Rename the remaining properties so their names don't necessarily match the RSS
  elements they map to. Instead, the names should be descriptive and easy to
  understand.
* :attr:`.Podcast.explicit` is now required, and is :obj:`bool`.
* Add shorthand for generating the RSS: Just try to converting your :class:`~podgen.Podcast`
  object to :obj:`str`!
* Expand the documentation.
* Move away from the extension framework, and rely on class inheritance instead.

.. _python-feedgen: https://github.com/lkiesow/python-feedgen
