import pytest
from django.http import HttpResponse
from django.views import View

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

    form_session_one.clear()

    form_session_two = helpers.FormSession(session_request)

    assert form_session_two.ingress_url == ''
    assert form_session_two.funnel_steps == []


class MyView(View):
    def get(self, *args, **kwargs):
        response = HttpResponse('Hello world')
        response.form_session = self.form_session
        return response


class FormSessionView(helpers.FormSessionMixin, MyView):
    pass


def test_form_session_mixin(session_request):
    response = FormSessionView.as_view()(session_request)

    assert isinstance(
        response.form_session, FormSessionView.form_session_class
    )


def test_form_ingress_url_mixin_set_if_http_referer(rf, client):
    request = rf.get('/foo/bar/', HTTP_REFERER='http://referer.com')
    request.session = {}
    response = FormSessionView.as_view()(request)

    assert response.form_session.ingress_url == 'http://referer.com'


def test_form_ingress_url_mixin_not_overrite(rf):
    session = {}
    request_one = rf.get('/foo/bar/a/', HTTP_REFERER='http://referer-a.com')
    request_one.session = session
    FormSessionView.as_view()(request_one)

    request_two = rf.get('/foo/bar/b/', HTTP_REFERER='http://referer-b.com')
    request_two.session = session
    response = FormSessionView.as_view()(request_two)

    assert response.form_session.ingress_url == 'http://referer-a.com'


def test_form_ingress_url_referer_header_missing(rf):
    request = rf.get('/foo/bar/')
    request.session = {}
    response = FormSessionView.as_view()(request)

    assert response.form_session.ingress_url is None
