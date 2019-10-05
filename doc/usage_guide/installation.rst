============
Installation
============

PodGen can be used on any system (if not: file a bug report!), and officially supports
Python 2.7 and 3.4, 3.5, 3.6 and 3.7.

Use `pip <https://pypi.python.org/pypi>`_::

    $ pip install podgen

Remember to use a `virtual environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_!

.. note::

   One of the dependencies of PodGen, `lxml <https://lxml.de/>`_, stopped supporting
   Python 3.4 in version 4.4.0. If you are installing PodGen using Python 3.4, you
   should select a compatible version of lxml by running e.g.::

      pip install 'lxml<4.4.0'

   The step "Running setup.py install for lxml" will take several minutes and
   `requires installation of building tools <https://lxml.de/installation.html>`_, since the lxml version does not include
   pre-built binaries.
