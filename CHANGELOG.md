# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
### Added

- This `CHANGELOG.md` file, for documenting notable changes.

### Removed

- Support for Python 3.3, due to its age and lack of support, and bugs with
  installing `tinytag`.

### Fixed

- `UnicodeEncodeError` when writing a podcast with non-ASCII characters to file
  in an environment where Python defaults to ASCII encoding.
- Incompatibility with unicode strings on Python 2.7.


## [1.0.0] - 2017-05-24
### Added

- The Podcast and Episode classes for easily generating a podcast out of data,
  and related utilities and classes.

[1.0.0]: https://github.com/tobinus/python-podgen/compare/290045ac...v1.0.0
