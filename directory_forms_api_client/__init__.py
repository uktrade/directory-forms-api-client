from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("forms_api_client")
except PackageNotFoundError:
    __version__ = 'dev'


from directory_forms_api_client.client import forms_api_client, get_forms_api_client

__all__ = ['forms_api_client', 'get_forms_api_client']
