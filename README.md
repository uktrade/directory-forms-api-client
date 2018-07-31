# directory-forms-api-client

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![snyk-image]][snyk]

**Directory forms API client for headless forms.**

---

## Requirements

## Installation

```shell
pip install directory_forms_api_client
```

## Usage

The api client must be passed into each form instance, so first set the the client settings:

| Setting                      | Notes                                                       |
| ---------------------------- | ----------------------------------------------------------- |
| DIRECTORY_FORMS_API_BASE_URL |                                                             |
| DIRECTORY_FORMS_API_API_KEY  | Unique to client. Retrieved during the on-boarding process. |


Once that is done the forms can be used.


### Submit to Zendesk

```python
from directory_forms_api_client import forms


class ZendeskForm(forms.ZendeskAPIForm):
    # note that the base form provides `requester_email` email field
    title = fields.CharField()


form = ZendeskForm(data={
    'title': 'example',
    'requester_email': 'three@example.com'
})
assert form.is_valid()
form.save()
```

### Send as email

#### Send to a user-submitted email address

```python
from directory_forms_api_client import forms

class EmailForm(forms.ZendeskAPIForm):
    title = fields.CharField()
    email = fields.EmailField()

form = TestForm(data={'title': 'Example', 'email': 'a@foo.com'})

assert form.is_valid()
form.save(submission_recipients=[form.cleaned_data['email']])

```

#### Send to a pre-defined email address
```python
from directory_forms_api_client import forms

class EmailForm(forms.EmailAPIForm):
    title = fields.CharField()

form = TestForm(data={'title': 'Example'})

assert form.is_valid()
form.save(submission_recipients=[settings.FEEDBACK_EMAIL_RECIPIENTS])

```

## Development

    $ git clone https://github.com/uktrade/directory-forms-api-client
    $ cd directory-forms-api-client
    # [create your virtual environment and activate it]
    $ pip install -e . # install the requirements defined in setup.py

### Testing

    $ make test


## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                     |
| --------------------------- |
| DIRECTORY_PYPI_USERNAME     |
| DIRECTORY_PYPI_PASSWORD     |

Then run the following command:

    make publish


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-forms-api-client/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-forms-api-client

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-forms-api-client/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-forms-api-client/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-forms-api-client/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-forms-api-client

[pypi-image]: https://badge.fury.io/py/directory-forms-api-client.svg
[pypi]: https://badge.fury.io/py/directory-forms-api-client

[snyk-image]: https://snyk.io/test/github/uktrade/directory-forms-api-client/badge.svg
[snyk]: https://snyk.io/test/github/uktrade/directory-forms-api-client
