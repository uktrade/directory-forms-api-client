from unittest import TestCase

from directory_forms_api_client.client import APIFormsClient
from tests import stub_request


class APIFormsClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://forms.com'
        self.api_key = 'test'
        self.client = APIFormsClient(self.base_url, self.api_key)

    @stub_request('https://forms.com/api/v1/healthcheck/ping/', 'get')
    def test_ping(self, stub):
        self.client.ping()

    @stub_request('https://forms.com/api/v1/generic/', 'post')
    def test_submit_generic(self, stub):
        data = {'field_one': 'value_one'}
        self.client.submit_generic(data)

        request = stub.request_history[0]
        assert request.json() == data
