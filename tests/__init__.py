import base64
from functools import wraps

import requests_mock


def stub_request(url, http_method, status_code=200):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with requests_mock.mock() as mock:
                mocked_method = getattr(mock, http_method)
                mocked_method(url, status_code=status_code)
                args += (mock,)
                return func(*args, **kwargs)
        return wrapper
    return decorator


class BasicAuthenticator:
    def __init__(self, username: str, password: str):
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode("ascii"))
        self.headers = {"Authorization": f"Basic {encoded_credentials.decode('ascii')}"}


basic_authenticator = BasicAuthenticator("user", "password")
