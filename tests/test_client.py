from unittest import TestCase

from directory_forms_api_client.client import APIFormsClient
import pkg_resources
from tests import stub_request


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

    def test_timeout(self):
        assert self.client.timeout == 4

    def test_sender_id(self):
        assert self.client.request_signer.sender_id == 'test'

    def test_version(self):
        assert APIFormsClient.version == pkg_resources.get_distribution(
            'directory-forms-api-client'
        ).version
