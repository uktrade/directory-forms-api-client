from unittest import mock

from directory_forms_api_client import backends, client


def test_email_backend_mixin_backend_class():
    mock_client = mock.Mock(spec_set=client.DirectoryFormsAPIClient)
    backend = backends.DirectoryFormsBackendEmail(
        recipients=['test@example.com'],
        client=mock_client,
    )

    backend.save({'field_one': 'value one', 'field_two': 'value two'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'field_one': 'value one', 'field_two': 'value two'},
        'meta': {
            'backend_name': 'email',
            'recipients': ['test@example.com']
        }
    })


def test_zendesk_backend_mixin_backend_class():

    mock_client = mock.Mock(spec_set=client.DirectoryFormsAPIClient)
    backend = backends.DirectoryFormsBackendZendesk(client=mock_client)

    backend.save({'requester_email': 'a@foo.com', 'field_two': 'value two'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'requester_email': 'a@foo.com', 'field_two': 'value two'},
        'meta': {'backend_name': 'zendesk'}
    })
