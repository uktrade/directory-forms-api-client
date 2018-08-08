import abc

from directory_forms_api_client.client import forms_api_client


class AbstractAction(abc.ABC):

    def __init__(self, client=forms_api_client, *args, **kwargs):
        self.client = client
        super().__init__(*args, **kwargs)

    def serialize_data(self, data):
        return {
            'data': data,
            'meta': self.meta
        }

    def save(self, data):
        serialized_data = self.serialize_data(data)
        return self.client.submit_generic(serialized_data)


class EmailAction(AbstractAction):

    def __init__(
        self, recipients, subject, reply_to, from_email, *args, **kwargs
    ):
        self.meta = {
            'action_name': 'email',
            'recipients': recipients,
            'subject': subject,
            'reply_to': reply_to,
            'from_email': from_email,
        }
        super().__init__(*args, **kwargs)


class ZendeskAction(AbstractAction):

    def __init__(self, subject, full_name, email_address, *args, **kwargs):
        self.meta = {
            'action_name': 'zendesk',
            'full_name': full_name,
            'email_address': email_address,
            'subject': subject,
        }
        super().__init__(*args, **kwargs)
