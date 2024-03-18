from django.forms import Form

from directory_forms_api_client import actions


class AbstractActionMixin:

    @property
    def action_class(self):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        action = self.action_class(*args, **kwargs)
        return action.save(self.serialized_data)

    @property
    def serialized_data(self):
        return self.cleaned_data


class SaveOnlyInDatabaseActionMixin(AbstractActionMixin):
    action_class = actions.SaveOnlyInDatabaseAction


class EmailActionMixin(AbstractActionMixin):
    action_class = actions.EmailAction

    @property
    def serialized_data(self):
        return {
            'text_body': self.text_body,
            'html_body': self.html_body,
        }

    @property
    def text_body(self):
        raise NotImplementedError()

    @property
    def html_body(self):
        raise NotImplementedError()


class ZendeskActionMixin(AbstractActionMixin):
    action_class = actions.ZendeskAction


class GovNotifyEmailActionMixin(AbstractActionMixin):
    action_class = actions.GovNotifyEmailAction


class GovNotifyBulkEmailActionMixin(AbstractActionMixin):
    action_class = actions.GovNotifyBulkEmailAction


class GovNotifyLetterActionMixin(AbstractActionMixin):
    action_class = actions.GovNotifyLetterAction


class PardotActionMixin(AbstractActionMixin):
    action_class = actions.PardotAction


class SaveOnlyInDatabaseAPIForm(SaveOnlyInDatabaseActionMixin, Form):
    pass


class EmailAPIForm(EmailActionMixin, Form):
    pass


class ZendeskAPIForm(ZendeskActionMixin, Form):
    pass


class GovNotifyEmailAPIForm(GovNotifyEmailActionMixin, Form):
    pass


class GovNotifyBulkEmailAPIForm(GovNotifyBulkEmailActionMixin, Form):
    pass


class GovNotifyLetterAPIForm(GovNotifyLetterActionMixin, Form):
    pass


class PardotAPIForm(PardotActionMixin, Form):
    pass
