from unittest import mock

import pytest

from directory_forms_api_client import actions, client, helpers


@pytest.fixture
def form_session(rf):
    request = rf.get('/')
    request.session = {
        'DIRECTORY_API_FORMS_FUNNEL_STEPS': ['one', 'two'],
        'DIRECTORY_API_FORMS_INGRESS_URL': 'example.com'
    }
    return helpers.FormSession(request=request)


def test_email_action_mixin_action_class(settings, form_session):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.EmailAction(
        recipients=['test@example.com'],
        client=mock_client,
        subject='a subject',
        reply_to=['reply_to@example.com'],
        form_url='/the/form/',
        form_session=form_session
    )

    action.save({'field_one': 'value one', 'field_two': 'value two'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'field_one': 'value one', 'field_two': 'value two'},
        'meta': {
            'action_name': 'email',
            'recipients': ['test@example.com'],
            'reply_to': ['reply_to@example.com'],
            'subject': 'a subject',
            'form_url': '/the/form/',
            'funnel_steps': ['one', 'two'],
            'ingress_url': 'example.com',
        }
    })


def test_zendesk_action_mixin_action_class(settings, form_session):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.ZendeskAction(
        client=mock_client,
        subject='a subject',
        full_name='jim example',
        email_address='jim@example.com',
        service_name='some service',
        form_url='/the/form/',
        form_session=form_session,
    )

    action.save({'requester_email': 'a@foo.com', 'field_two': 'value two'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'requester_email': 'a@foo.com', 'field_two': 'value two'},
        'meta': {
            'action_name': 'zendesk',
            'subject': 'a subject',
            'full_name': 'jim example',
            'email_address': 'jim@example.com',
            'service_name': 'some service',
            'form_url': '/the/form/',
            'funnel_steps': ['one', 'two'],
            'ingress_url': 'example.com',
        }
    })


def test_zendesk_action_mixin_action_class_subdomain(settings, form_session):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.ZendeskAction(
        client=mock_client,
        subject='a subject',
        full_name='jim example',
        email_address='jim@example.com',
        service_name='some service',
        subdomain='some-sobdomain',
        form_url='/the/form/',
        form_session=form_session,
    )

    action.save({'requester_email': 'a@foo.com', 'field_two': 'value two'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'requester_email': 'a@foo.com', 'field_two': 'value two'},
        'meta': {
            'action_name': 'zendesk',
            'subject': 'a subject',
            'full_name': 'jim example',
            'email_address': 'jim@example.com',
            'subdomain': 'some-sobdomain',
            'service_name': 'some service',
            'form_url': '/the/form/',
            'funnel_steps': ['one', 'two'],
            'ingress_url': 'example.com',
        }
    })


def test_gov_notify_action_mixin_action_class(settings, form_session):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.GovNotifyAction(
        client=mock_client,
        template_id='123456',
        email_address='jim@example.com',
        email_reply_to_id='123',
        form_url='/the/form/',
        form_session=form_session,
    )

    action.save({'name': 'hello'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'name': 'hello'},
        'meta': {
            'action_name': 'gov-notify',
            'template_id': '123456',
            'email_address': 'jim@example.com',
            'email_reply_to_id': '123',
            'form_url': '/the/form/',
            'funnel_steps': ['one', 'two'],
            'ingress_url': 'example.com',
        }
    })


def test_gov_notify_action_mixin_action_class_no_reply_id(
    settings, form_session
):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.GovNotifyAction(
        client=mock_client,
        template_id='123456',
        email_address='jim@example.com',
        form_url='/the/form/',
        form_session=form_session,
    )

    action.save({'name': 'hello'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'name': 'hello'},
        'meta': {
            'action_name': 'gov-notify',
            'template_id': '123456',
            'email_address': 'jim@example.com',
            'form_url': '/the/form/',
            'funnel_steps': ['one', 'two'],
            'ingress_url': 'example.com',
        }
    })


def test_pardot_action_mixin_action_class(settings, form_session):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.PardotAction(
        client=mock_client,
        pardot_url='http://www.example.com/some/submission/path/',
        form_url='/the/form/',
        form_session=form_session,
    )

    action.save({'name': 'hello'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'name': 'hello'},
        'meta': {
            'action_name': 'pardot',
            'pardot_url': 'http://www.example.com/some/submission/path/',
            'form_url': '/the/form/',
            'funnel_steps': ['one', 'two'],
            'ingress_url': 'example.com',
        }
    })
