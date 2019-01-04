from unittest import mock

import pytest

from django.forms import Form, fields

from directory_forms_api_client import actions, forms


@pytest.fixture
def mock_action_class():
    return mock.Mock(spec=actions.AbstractAction)


def test_email_action_form():
    expected_class = actions.EmailAction
    assert forms.EmailActionMixin.action_class is expected_class


def test_zendesk_action_form():
    expected_class = actions.ZendeskAction
    assert forms.ZendeskActionMixin.action_class is expected_class


@pytest.mark.parametrize('classes', (
    [forms.EmailActionMixin, Form],
    [forms.EmailAPIForm]
))
def test_email_action_mixin_user_submitted_email(classes, mock_action_class):

    class TestForm(*classes):
        action_class = mock_action_class

        title = fields.CharField()
        email = fields.EmailField()

        @property
        def text_body(self):
            return self.cleaned_data['title']

        @property
        def html_body(self):
            return '<a>' + self.cleaned_data['title'] + '</a>'

    form = TestForm(data={'title': 'Example', 'email': 'a@foo.com'})
    form_session = {}

    assert form.is_valid()

    form.save(
        recipients=[form.cleaned_data['email']],
        subject='a subject',
        reply_to=['reply_to@example.com'],
        form_url='/the/form/',
        form_session=form_session,
    )

    assert mock_action_class.call_count == 1
    assert mock_action_class.call_args == mock.call(
        recipients=['a@foo.com'],
        subject='a subject',
        reply_to=['reply_to@example.com'],
        form_url='/the/form/',
        form_session=form_session,
    )
    assert mock_action_class().save.call_count == 1
    assert mock_action_class().save.call_args == mock.call(
        form.serialized_data
    )


@pytest.mark.parametrize('classes', (
    [forms.EmailActionMixin, Form],
    [forms.EmailAPIForm]
))
def test_email_action_mixin_environment_defined_email(
    classes, mock_action_class
):

    class TestForm(*classes):
        action_class = mock_action_class

        title = fields.CharField()

        @property
        def text_body(self):
            return self.cleaned_data['title']

        @property
        def html_body(self):
            return '<a>' + self.cleaned_data['title'] + '</a>'

    form = TestForm(data={'title': 'Example'})
    form_session = {}

    assert form.is_valid()

    form.save(
        recipients=['a@bar.com'],
        subject='a subject',
        reply_to=['reply_to@example.com'],
        form_url='/the/form/',
        form_session=form_session,
    )

    assert mock_action_class.call_count == 1
    assert mock_action_class.call_args == mock.call(
        recipients=['a@bar.com'],
        subject='a subject',
        reply_to=['reply_to@example.com'],
        form_url='/the/form/',
        form_session=form_session,
    )
    assert mock_action_class().save.call_count == 1
    assert mock_action_class().save.call_args == mock.call(
        form.serialized_data
    )


@pytest.mark.parametrize('classes', (
    [forms.ZendeskActionMixin, Form],
    [forms.ZendeskAPIForm]
))
def test_zendesk_action_mixin(classes, mock_action_class):

    class TestForm(*classes):
        action_class = mock_action_class

        title = fields.CharField()

    data = {
        'title': 'Example',
        'email_address': 'three@example.com',
        'full_name': 'Jim Example',
        'subject': 'hello there',
    }
    form = TestForm(data=data)
    form_session = {}

    assert form.is_valid()

    form.save(
        full_name=data['full_name'],
        email_address=data['email_address'],
        subject=data['subject'],
        service_name='some service',
        form_url='/the/form/',
        form_session=form_session,
    )

    assert mock_action_class.call_count == 1
    assert mock_action_class.call_args == mock.call(
        full_name=data['full_name'],
        email_address=data['email_address'],
        subject=data['subject'],
        service_name='some service',
        subdomain=None,
        form_url='/the/form/',
        form_session=form_session,
    )
    assert mock_action_class().save.call_count == 1
    assert mock_action_class().save.call_args == mock.call(form.cleaned_data)


@pytest.mark.parametrize('classes', (
    [forms.EmailActionMixin, Form],
    [forms.EmailAPIForm]
))
def test_email_action_mixin_not_implemented(classes, mock_action_class):

    class TestForm(*classes):
        action_class = mock_action_class

        title = fields.CharField()

    form = TestForm()

    with pytest.raises(NotImplementedError):
        form.text_body()

    with pytest.raises(NotImplementedError):
        form.html_body()


@pytest.mark.parametrize('classes', (
    [forms.GovNotifyActionMixin, Form],
    [forms.GovNotifyAPIForm]
))
def test_gov_notify_action(classes, mock_action_class):

    class TestForm(*classes):
        action_class = mock_action_class

        title = fields.CharField()

    data = {
        'email_address': 'three@example.com',
        'template_id': '123456',
        'title': 'some title',
    }
    form_session = {}

    form = TestForm(data)
    assert form.is_valid()

    form.save(
        template_id=data['template_id'],
        email_address=data['email_address'],
        email_reply_to_id='123',
        form_url='/the/form/',
        form_session=form_session,
    )

    assert mock_action_class.call_count == 1
    assert mock_action_class.call_args == mock.call(
        template_id=data['template_id'],
        email_address=data['email_address'],
        email_reply_to_id='123',
        form_url='/the/form/',
        form_session=form_session,
    )
    assert mock_action_class().save.call_count == 1
    assert mock_action_class().save.call_args == mock.call(form.cleaned_data)


@pytest.mark.parametrize('classes', (
    [forms.GovNotifyActionMixin, Form],
    [forms.GovNotifyAPIForm]
))
def test_gov_notify_action_no_reply_to_id(classes, mock_action_class):

    class TestForm(*classes):
        action_class = mock_action_class

        title = fields.CharField()

    data = {
        'email_address': 'three@example.com',
        'template_id': '123456',
        'title': 'some title',
    }
    form = TestForm(data)
    form_session = {}

    assert form.is_valid()

    form.save(
        template_id=data['template_id'],
        email_address=data['email_address'],
        form_url='/the/form/',
        form_session=form_session,
    )

    assert mock_action_class.call_count == 1
    assert mock_action_class.call_args == mock.call(
        template_id=data['template_id'],
        email_address=data['email_address'],
        email_reply_to_id=None,
        form_url='/the/form/',
        form_session=form_session,
    )
    assert mock_action_class().save.call_count == 1
    assert mock_action_class().save.call_args == mock.call(form.cleaned_data)


@pytest.mark.parametrize('classes', (
    [forms.PardotActionMixin, Form],
    [forms.PardotAPIForm]
))
def test_pardot_action(classes, mock_action_class):

    class TestForm(*classes):
        action_class = mock_action_class

        title = fields.CharField()

    data = {
        'email_address': 'three@example.com',
        'template_id': '123456',
        'title': 'some title',
    }
    form_session = {}
    form = TestForm(data)

    assert form.is_valid()

    form.save(
        pardot_url='http://www.example.com/some/submission/path/',
        form_url='/the/form/',
        form_session=form_session
    )

    assert mock_action_class.call_count == 1
    assert mock_action_class.call_args == mock.call(
        pardot_url='http://www.example.com/some/submission/path/',
        form_url='/the/form/',
        form_session=form_session,
    )
    assert mock_action_class().save.call_count == 1
    assert mock_action_class().save.call_args == mock.call(form.cleaned_data)
