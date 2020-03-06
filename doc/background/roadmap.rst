-------
Roadmap
-------

When PodGen reaches a certain point where it has all the features it needs,
while still being simple to use, it would not be necessary with further
updates… had it not been for changes to PodGen's dependencies and changes to
the overall podcast standards. Luckily, the applications that read podcasts
tend to be backwards compatible, in order to support all the old podcasts that
are out there.

The current plan for PodGen updates is as follows:

* **New minor version**: Support for the new Apple Podcast specifications,
  as much as is possible without breaking backwards compatibility.
* Deprecation warnings for properties and such which will be removed in the
  next major version.
* **New major version**: Support for the new Apple Podcast specifications which
  could not be included earlier due to backwards compatibility,
  or which have new names or behaviours to simplify the API. Removal of
  deprecated features.
* **New minor versions**: Removal of support for Python releases that have
  passed `End of Life`_ (Python 2.7 after January 1st 2020, Python
  3.4), allowing for simplifications and use of new features in the code base.
  Other code and documentation improvements should hopefully stop PodGen from
  becoming stale and burdensome to maintain.
* Better ways of adding support for RSS features which PodGen itself does not
  support.

.. _End of life: https://devguide.python.org/#status-of-python-branches

Unlike other libraries with evolving demands, PodGen is expected to stay
relatively stable with the occasional update. Changes to the Apple Podcast
specifications do not occur particularly often, so PodGen won't need to change
often either.

Since PodGen is an open source project and its maintainer has a limited amount
of time to spare, updates may be sporadic. Despite this, please don't hesitate
to report issues or feature requests if there is something that does not
work or you feel should be included. The project is used by the Student Radio
of Trondheim and will be kept up-to-date with their requirements, though they
are not primarily a podcast producer.
