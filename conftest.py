def pytest_configure():
    from django.conf import settings
    settings.configure(
        URLS_EXCLUDED_FROM_SIGNATURE_CHECK=[],
        USE_I18N=False,
        DIRECTORY_FORMS_API_BASE_URL='https://example.com',
        DIRECTORY_FORMS_API_API_KEY='debug',
    )
