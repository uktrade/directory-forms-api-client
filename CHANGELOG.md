# Changelog

## [4.1.1](https://pypi.org/project/directory-forms-api-client/4.1.1/) (2019-07-04)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/22/files)

### Implemented enhancements
- TT-1559 - Improve Directory Forms API documentation
- No ticket - Can now import the instantiated client as `from directory_sso_api_client import sso_api_client`
- No ticket - Remove `version.py`

### Bugs fixed
- No ticket - Upgrade vulnerable django version to django 1.11.22


## [4.1.0](https://pypi.org/project/directory-forms-api-client/4.1.0/) (2019-06-12)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/21/files)

### Implemented enhancements
- Updated test requirements to test against Django 2.2

## [4.0.0](https://pypi.org/project/directory-forms-api-client/4.0.0/) (2019-04-23)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/20/files)

### Implemented enhancements
- Upgraded directory client core to reduce overzealous logging from the fallback cache.
- Improved documentation in readme.
- The client responses are now subclasses of `request.Response`.

**Breaking changes:**

- Directory client core has been upgraded a major version 5.0.0. [See](https://github.com/uktrade/directory-client-core/pull/16)
- Dropped support for Python 3.5
- The client responses dropped the `raw_response` property. The attributes of `raw_response` are now available on the client responses.
