# Changelog

## [7.2.0](https://pypi.org/project/directory-forms-api-client/7.2.1/) (2023-07-05)
[Full Changelog](
- KLS-822 - Update Django to 4.2.3 and use at lease 7.2.4 of directory-client-core

## [7.2.0](https://pypi.org/project/directory-forms-api-client/7.2.0/) (2022-05-23)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/41)
- KLS-622 - Update Django to 4.2

## [7.1.0](https://pypi.org/project/directory-forms-api-client/7.1.0/) (2022-08-19)
[Full Changelog](https://github.com/uktrade/directory-sso-api-client/releases/tag/v7.1.0)
- GLS-386 - Update maximum version of directory_client_core for Django 3.2 upgrade

## [7.0.0](https://pypi.org/project/directory-forms-api-client/7.0.0/) (2022-08-19)
[Full Changelog](https://github.com/uktrade/directory-sso-api-client/releases/tag/v7.0.0)
- GLS-386 - Update for use with Django 3.2

## [6.2.0](https://pypi.org/project/directory-forms-api-client/6.2.0/) (2022-03-25)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/36/files)
- GPL-151 - Added deprecation message for EmailAction

## [6.1.0](https://pypi.org/project/directory-forms-api-client/6.1.0/) (2021-06-09)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/34/files)
- GP2-2718 - Data retention - added new endpoint

## [6.0.0](https://pypi.org/project/directory-forms-api-client/6.0.0/) (2020-12-17)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/31/files)
- GBAU-893 - Fixed SaveInDatabaseOnly actions


## [5.4.0](https://pypi.org/project/directory-forms-api-client/5.4.0/) (2020-10-02)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/30/files)
- No ticket - bump django version and core version in setup.py so Django 3.x can start using this package


## [5.3.0](https://pypi.org/project/directory-forms-api-client/5.3.0/) (2020-03-16)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/28/files)

### Implemented enhancements

* XOT-1277 - Add ability to send data only to database


## [5.2.0](https://pypi.org/project/directory-forms-api-client/5.2.0/) (2020-02-18)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/27/files)

### Implemented enhancements

* TT-2288 add support for custom authenticators

## [5.1.0](https://pypi.org/project/directory-forms-api-client/5.1.0/) (2019-10-22)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/26/files)
TT-2042 add sender-ip-address for rate limiting

## [5.0.0](https://pypi.org/project/directory-forms-api-client/5.0.0/) (2019-07-16)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/25/files)

**Implemented enhancements:**

## Breaking changes
TT-1604 send letter via gov notify
TT-1604 govnotifyemailaction replaces GovNotifyAction
    - GovNotifyActionMixin has renamed to GovNotifyEmailActionMixin
    - GovNotifyAPIForm has renamed to GovNotifyEmailAPIForm
    - directory_client_core upgraded from 5 to 6

## [4.1.1](https://pypi.org/project/directory-forms-api-client/4.1.1/) (2019-07-04)
[Full Changelog](https://github.com/uktrade/directory-forms-api-client/pull/22/files)

### Implemented enhancements
- TT-1599 - Improve Directory Forms API documentation
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
