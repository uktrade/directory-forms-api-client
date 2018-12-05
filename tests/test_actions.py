from unittest import mock

from directory_forms_api_client import actions, client


def test_email_action_mixin_action_class(settings):
    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.EmailAction(
        recipients=['test@example.com'],
        client=mock_client,
        subject='a subject',
        reply_to=['reply_to@example.com'],
        form_url='/the/form/',
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
        }
    })


def test_zendesk_action_mixin_action_class(settings):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.ZendeskAction(
        client=mock_client,
        subject='a subject',
        full_name='jim example',
        email_address='jim@example.com',
        service_name='some service',
        form_url='/the/form/',
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
        }
    })


def test_zendesk_action_mixin_action_class_subdomain(settings):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.ZendeskAction(
        client=mock_client,
        subject='a subject',
        full_name='jim example',
        email_address='jim@example.com',
        service_name='some service',
        subdomain='some-sobdomain',
        form_url='/the/form/',
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
        }
    })


def test_gov_notify_action_mixin_action_class(settings):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.GovNotifyAction(
        client=mock_client,
        template_id='123456',
        email_address='jim@example.com',
        email_reply_to_id='123',
        form_url='/the/form/',
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
        }
    })


def test_gov_notify_action_mixin_action_class_no_reply_id(settings):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.GovNotifyAction(
        client=mock_client,
        template_id='123456',
        email_address='jim@example.com',
        form_url='/the/form/',
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
        }
    })


def test_pardot_action_mixin_action_class(settings):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.PardotAction(
        client=mock_client,
        pardot_url='http://www.example.com/some/submission/path/',
        form_url='/the/form/',
    )

    action.save({'name': 'hello'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'name': 'hello'},
        'meta': {
            'action_name': 'pardot',
            'pardot_url': 'http://www.example.com/some/submission/path/',
            'form_url': '/the/form/',
        }
    })
