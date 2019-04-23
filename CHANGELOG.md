# Changelog

## [4.0.0](https://pypi.org/project/directory-forms-api-client/4.0.0/) (2019-04-23)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/20/files)

**Implemented enhancements:**

- Upgraded directory client core to reduce overzealous logging from the fallback cache.
- Improved documentation in readme.
- The client responses are now subclasses of `request.Response`.

**Breaking changes:**

- Directory client core has been upgraded a major version 5.0.0. [See](https://github.com/uktrade/directory-client-core/pull/16)
- Dropped support for Python 3.5
- The client responses dropped the `raw_response` property. The attributes of `raw_response` are now available on the client responses.
