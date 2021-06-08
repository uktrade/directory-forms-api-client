import pkg_resources

from directory_forms_api_client.client import APIFormsClient

from tests import basic_authenticator, stub_request
from unittest import TestCase


class APIFormsClientTest(TestCase):

    def setUp(self):
        self.client = APIFormsClient(
            base_url='https://forms.com',
            api_key='test',
            sender_id='test',
            timeout=4,
        )

    @stub_request('https://forms.com/api/healthcheck/ping/', 'get')
    def test_ping(self, stub):
        self.client.ping()

    @stub_request('https://forms.com/api/submission/', 'post')
    def test_submit_generic(self, stub):
        data = {'field_one': 'value_one'}
        self.client.submit_generic(data)

        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://forms.com/api/healthcheck/ping/', 'get')
    def test_ping_with_authenticator(self, stub):
        self.client.ping(authenticator=basic_authenticator)
        request = stub.request_history[0]
        assert 'Authorization' in request.headers
        assert request.headers['Authorization'].startswith('Basic ')

    @stub_request('https://forms.com/api/submission/', 'post')
    def test_submit_generic_with_authenticator(self, stub):
        data = {'field_one': 'value_one'}
        self.client.submit_generic(data, authenticator=basic_authenticator)

        request = stub.request_history[0]
        assert 'Authorization' in request.headers
        assert request.headers['Authorization'].startswith('Basic ')

    @stub_request('https://forms.com/api/delete-submissions/test@gmail.com/', 'delete')
    def test_delete_form_with_authenticator(self, stub):
        self.client.delete_submissions(
            email_address='test@gmail.com', authenticator=basic_authenticator)

        request = stub.request_history[0]
        assert 'Authorization' in request.headers
        assert request.headers['Authorization'].startswith('Basic ')

    def test_timeout(self):
        assert self.client.timeout == 4

    def test_sender_id(self):
        assert self.client.request_signer.sender_id == 'test'

    def test_version(self):
        assert APIFormsClient.version == pkg_resources.get_distribution(
            'directory-forms-api-client'
        ).version
