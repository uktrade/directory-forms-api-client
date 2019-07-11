# directory-forms-api-client

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![semver-image]][semver]

**Directory forms API client for headless forms.**

---

## Requirements

## Installation

    $ pip install directory_forms_api_client

## Client Enrollment
The api client must be created in directory-forms-api's admin panel to access `DIRECTORY_FORMS_API_API_KEY` and `DIRECTORY_FORMS_API_SENER_ID`.

![Enrol-api-client](secret.gif)

## Usage

The api client must be passed into each form instance, so first set the the client settings:

| Setting                           | Notes                                                       |
| --------------------------------- | ----------------------------------------------------------- |
| `DIRECTORY_FORMS_API_BASE_URL`    |                                                             |
| `DIRECTORY_FORMS_API_API_KEY`     | Unique to client. Retrieved during the on-boarding process. |
| `DIRECTORY_FORMS_API_SENDER_ID`   | Unique to client. Retrieved during the on-boarding process. |
| `DIRECTORY_FORMS_DEFAULT_TIMEOUT` |                                                             |

The following [directory client core settings](https://github.com/uktrade/directory-client-core) also apply to directory cms client:

| Setting                                              | Notes                                                 |
| -----------------------------------------------------| ------------------------------------------------------|
| `DIRECTORY_CLIENT_CORE_CACHE_EXPIRE_SECONDS`         | Duration to store the retrieved content in the cache. |    |
| `DIRECTORY_CLIENT_CORE_CACHE_LOG_THROTTLING_SECONDS` | Duration to throttle log events for a given url for.  |

Once that is done the forms can be used.

### Submit to Zendesk

```python
from directory_forms_api_client import forms


class ZendeskForm(forms.ZendeskAPIForm):
    # note that the base form provides `requester_email` email field
    title = fields.CharField()


form = ZendeskForm(data={
    'name': 'Example Person',
    'email': 'three@example.com'
})
assert form.is_valid()
form.save(
    email_address=form.cleaned_data['email'],
    full_name='Example Person',
    subject='Bo in the house',
    service_name='Foo Bar',
)
```

#### Different subdomain

The default behaviour of Forms API is to use the default configured zendesk subdomain when creating the tickets. To use a different subdomain, provide `subdomain`:

```python
form.save(
    email_address=form.cleaned_data['email'],
    full_name='Example Person',
    subject='Some ticket subject',
    subdomain='some-other-subdomain',
)
```

Note that Forms API must first be configured to expect the provided subdomain.

### Send as email

#### Send to a user-submitted email address

```python
from directory_forms_api_client import forms

class EmailForm(forms.ZendeskAPIForm):
    title = fields.CharField()
    email = fields.EmailField()
    
    @property
    def text_body(self):
        ''' Override text_body to text templte of email body.'''
        text = []
        for key, value in self.cleaned_data.items():
            text.append(key)
            text.append(str(value))
            text.append('\n')
        text = ' '.join(text)
        self.cleaned_data['text_body'] = text
        return text_body

    @property
    def html_body(self):
        ''' Override html_body to return html template of email body.'''
        cleaned_html = []
        for key, value in self.cleaned_data.items():
            cleaned_html.append('<p>')
            cleaned_html.append(key)
            cleaned_html.append(':')
            cleaned_html.append(str(value))
            cleaned_html.append('</p>')
        self.cleaned_data['html_body'] = ''.join(cleaned_html)
        return cleaned_html


form = TestForm(data={'title': 'Example', 'email': 'a@foo.com'})

assert form.is_valid()
form.save(
    recipients=[form.cleaned_data['email']],
    subject='Some email subject',
    reply_to=['reply@example.com'],
    service_name='Foo Bar',
    form_url=self.request.get_full_path()
)

```

You can also use `EmailActionMixin` or `EmailAction` directly for more complex requirements. For e.g. When creating form when inheriting from another form or collecting data from multi-step forms (where any one form doesn't have the complete data).
See [here](https://github.com/uktrade/great-domestic-ui/blob/develop/contact/views.py#L268) for an example.


#### Send to a pre-defined email address
```python
from directory_forms_api_client import forms

class EmailForm(forms.EmailAPIForm):
    title = fields.CharField()
    
    @property
    def text_body(self):
        ''' Override text_body to text templte of email body.'''
        
        text = 'title: ' + str(self.cleaned_data['title'])
        return text

    @property
    def html_body(self):
        ''' Override html_body to return html template of email body.'''
        
        cleaned_html = '<p>title: ' + str(self.cleaned_data['title']) + '</p>'
        return cleaned_html

form = TestForm(data={'title': 'Example'})

assert form.is_valid()
form.save(submission_recipients=[settings.FEEDBACK_EMAIL_RECIPIENTS])

```

### Send via gov.uk Notify

```python
from directory_forms_api_client import forms

class GovNotifyForm(forms.GovNotifyAPIForm):
    title = fields.CharField()
    email = fields.EmailField()

form = TestForm(data={'title': 'Example', 'email': 'a@foo.com'})

assert form.is_valid()
form.save(
    template_id='some-template-id-from-gov-notify',
    email_address=form.cleaned_data['email'],
)
```

## Spam checking

Spam checking can be activated by including a `spam_contol` object in the submission:

```py
    from directory_forms_api_client import helpers

    spam_control = helpers.SpamControl(
        # data that is worth spam checking
        contents=[form.cleaned_data['comment']],
    )
    form.save(
        template_id=data['template_id'],
        email_address=data['email_address'],
        form_url='/the/form/',
        spam_control=spam_control,
    )
```

This will result in the content being checked for spam before the submission is sent.

## Senders

Reporting on the submissions of specific senders can be facilitated by including a `sender` object in the submission.

```py
    from directory_forms_api_client import helpers

    sender = helpers.Sender(
        email_address=[form.cleaned_data['email_address']],
        country_code=forms.cleaned_data['country']
    )
    form.save(
        template_id=data['template_id'],
        email_address=data['email_address'],
        form_url='/the/form/',
        sender=sender,
    )
```

This allows for country-specific data retention policies to be respected, and to improve spam control functionality.


## Development

    $ git clone https://github.com/uktrade/directory-forms-api-client
    $ cd directory-forms-api-client
    # [create your virtual environment and activate it]
    $ pip install -e . # install the requirements defined in setup.py

### Testing

    $ make test


## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                       |
| ----------------------------- |
| `DIRECTORY_PYPI_USERNAME`     |
| `DIRECTORY_PYPI_PASSWORD`     |

Then run the following command:

    $ make publish


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-forms-api-client/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-forms-api-client

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-forms-api-client/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-forms-api-client/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-forms-api-client/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-forms-api-client

[pypi-image]: https://badge.fury.io/py/directory-forms-api-client.svg
[pypi]: https://badge.fury.io/py/directory-forms-api-client

[semver-image]: https://img.shields.io/badge/Versioning%20strategy-SemVer-5FBB1C.svg
[semver]: https://semver.org
