import pytest

from django.views import View
from django.http import HttpResponse
from directory_forms_api_client import helpers


@pytest.fixture
def session_request(rf):
    request = rf.get('/')
    request.session = {}
    return request


def test_form_session_set_ingress_url(session_request):
    form_session_one = helpers.FormSession(session_request)
    form_session_one.ingress_url = 'example.com'

    assert form_session_one.ingress_url == 'example.com'

    form_session_two = helpers.FormSession(session_request)

    assert form_session_two.ingress_url == 'example.com'


def test_form_session_unset_ingress_url(session_request):
    form_session_one = helpers.FormSession(session_request)
    form_session_one.ingress_url = 'example.com'

    assert form_session_one.ingress_url == 'example.com'

    del form_session_one.ingress_url

    assert form_session_one.ingress_url == ''

    form_session_two = helpers.FormSession(session_request)

    assert form_session_two.ingress_url == ''


def test_form_session_set_funnel_steps(session_request):
    form_session_one = helpers.FormSession(session_request)

    form_session_one.funnel_steps.append('one')
    form_session_one.funnel_steps.append('two')
    form_session_one.funnel_steps.append('three')

    assert form_session_one.funnel_steps == ['one', 'two', 'three']

    form_session_two = helpers.FormSession(session_request)

    assert form_session_two.funnel_steps == ['one', 'two', 'three']


def test_form_session_unset_funnel_steps(session_request):
    form_session_one = helpers.FormSession(session_request)

    form_session_one.funnel_steps.append('one')
    form_session_one.funnel_steps.append('two')
    form_session_one.funnel_steps.append('three')
    del form_session_one.funnel_steps

    assert form_session_one.funnel_steps == []

    form_session_two = helpers.FormSession(session_request)

    assert form_session_two.funnel_steps == []


def test_form_session_unset_all(session_request):
    form_session_one = helpers.FormSession(session_request)
    form_session_one.funnel_steps.append('one')
    form_session_one.ingress_url = 'example.com'

    del form_session_one

    form_session_two = helpers.FormSession(session_request)

    assert form_session_two.ingress_url == ''
    assert form_session_two.funnel_steps == []


def test_form_session_mixin(session_request):
    class TestView(helpers.FormSessionMixin, View):
        def get(self, *args, **kwargs):
            response = HttpResponse('Hello world')
            response.form_session = self.form_session
            return response

    view = TestView.as_view()
    response = view(session_request)

    assert isinstance(response.form_session, TestView.form_session_class)
