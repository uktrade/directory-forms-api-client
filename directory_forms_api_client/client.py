from directory_forms_api_client import __version__
from directory_client_core.base import AbstractAPIClient
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class APIFormsClient(AbstractAPIClient):

    endpoints = {
        # API V1 endpoints
        'ping': 'api/healthcheck/ping/',
        'submission': 'api/submission/',
        'delete_submissions': 'api/delete-submissions/',
        # API V2 endpoints
        'gov_notify_bulk_email': 'api/v2/gov-notify-bulk-email/',
        'hcsat_feedback_submission': 'api/v2/hcsat-feedback-submission/',
        'verification_reminders': 'api/v2/verification-reminders/',
    }
    version = __version__

    # API V1
    def ping(self, authenticator=None):
        return self.get(url=self.endpoints['ping'], authenticator=authenticator)

    def submit_generic(self, data, authenticator=None):
        return self.post(url=self.endpoints['submission'], data=data, authenticator=authenticator)

    def delete_submissions(self, email_address, authenticator=None):
        endpoint = self.endpoints['delete_submissions'] + f'{email_address}/'
        return self.delete(url=endpoint, authenticator=authenticator)

    # API V2
    def gov_notify_bulk_email(self, data, authenticator=None):
        """
        Allows an email with multiple recipients to be sent be gov.notify.

        :param data: Email meta data.
        :param authenticator: API authenticator class (default None)
        :return: Request object
        """

        return self.post(url=self.endpoints['gov_notify_bulk_email'], data=data, authenticator=authenticator)

    def hcsat_feedback_submission(self, data, authenticator=None):
        return self.post(url=self.endpoints['hcsat_feedback_submission'], data=data, authenticator=authenticator)

    def verification_reminders(self, data, authenticator=None):
        return self.post(url=self.endpoints['verification_reminders'], data=data, authenticator=authenticator)


forms_api_client = APIFormsClient(
    base_url=settings.DIRECTORY_FORMS_API_BASE_URL,
    api_key=settings.DIRECTORY_FORMS_API_API_KEY,
    sender_id=settings.DIRECTORY_FORMS_API_SENDER_ID,
    timeout=settings.DIRECTORY_FORMS_API_DEFAULT_TIMEOUT,
)

REQUIRED_SETTINGS = (
    'DIRECTORY_FORMS_API_BASE_URL',
    'DIRECTORY_FORMS_API_API_KEY',
    'DIRECTORY_FORMS_API_SENDER_ID',
)


def _get_required_setting(name: str):  # pragma: no cover
    if not hasattr(settings, name):
        raise ImproperlyConfigured(f'Missing required setting for BG Profile client: {name}')
    return getattr(settings, name)


def get_forms_api_client() -> APIFormsClient:  # pragma: no cover
    """
    Factory function to avoid import-time failures and
    make testing easier.
    """
    # Validate required settings explicitly
    base_url = _get_required_setting('DIRECTORY_FORMS_API_BASE_URL')
    api_key = _get_required_setting('DIRECTORY_FORMS_API_API_KEY')
    sender_id = _get_required_setting('DIRECTORY_FORMS_API_SENDER_ID')
    timeout = getattr(settings, 'DIRECTORY_FORMS_API_DEFAULT_TIMEOUT', 10)

    return APIFormsClient(
        base_url=base_url,
        api_key=api_key,
        sender_id=sender_id,
        timeout=timeout,
    )
