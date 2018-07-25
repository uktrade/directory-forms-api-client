from unittest import mock

import pytest

from django.forms import Form, fields

from directory_forms_api_client import backends, forms


@pytest.fixture
def mock_backend_class():
    return mock.Mock(spec=backends.AbstractBackend)


def test_email_backend_form():
    expected_class = backends.EmailBackend
    assert forms.EmailBackendMixin.backend_class is expected_class


def test_zendesk_backend_form():
    expected_class = backends.ZendeskBackend
    assert forms.ZendeskBackendMixin.backend_class is expected_class


@pytest.mark.parametrize('classes', (
    [forms.EmailBackendMixin, Form],
    [forms.EmailAPIForm]
))
def test_email_backend_mixin_user_submitted_email(
    classes, mock_backend_class
):

    class TestForm(*classes):
        backend_class = mock_backend_class

        title = fields.CharField()
        email = fields.EmailField()

    form = TestForm(data={'title': 'Example', 'email': 'a@foo.com'})

    assert form.is_valid()

    form.save(submission_recipients=[form.cleaned_data['email']])

    assert mock_backend_class.call_count == 1
    assert mock_backend_class.call_args == mock.call(recipients=['a@foo.com'])
    assert mock_backend_class().save.call_count == 1
    assert mock_backend_class().save.call_args == mock.call(form.cleaned_data)


@pytest.mark.parametrize('classes', (
    [forms.EmailBackendMixin, Form],
    [forms.EmailAPIForm]
))
def test_email_backend_mixin_environment_defined_email(
    classes, mock_backend_class
):

    class TestForm(*classes):
        backend_class = mock_backend_class

        title = fields.CharField()

    form = TestForm(data={'title': 'Example'})

    assert form.is_valid()

    form.save(submission_recipients=['a@bar.com'])

    assert mock_backend_class.call_count == 1
    assert mock_backend_class.call_args == mock.call(recipients=['a@bar.com'])
    assert mock_backend_class().save.call_count == 1
    assert mock_backend_class().save.call_args == mock.call(form.cleaned_data)


@pytest.mark.parametrize('classes', (
    [forms.ZendeskBackendMixin, Form],
    [forms.ZendeskAPIForm]
))
def test_zendesk_backend_mixin(classes, mock_backend_class):

    class TestForm(*classes):
        backend_class = mock_backend_class

        title = fields.CharField()

    form = TestForm(
        data={'title': 'Example', 'requester_email': 'three@example.com'}
    )

    assert form.is_valid()

    form.save()

    assert mock_backend_class.call_count == 1
    assert mock_backend_class.call_args == mock.call()
    assert mock_backend_class().save.call_count == 1
    assert mock_backend_class().save.call_args == mock.call(form.cleaned_data)
