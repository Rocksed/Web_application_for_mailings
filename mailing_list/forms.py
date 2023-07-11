from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from mailing_list.models import MESSAGE, CLIENT, SETTINGS


class SettingsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Submit('submit', 'Submit', css_class='btn-primary')
        )

    class Meta:
        model = SETTINGS
        exclude = ['author', 'last_run']


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Submit('submit', 'Submit', css_class='btn-primary')
        )

    class Meta:
        model = MESSAGE
        fields = '__all__'


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Submit('submit', 'Submit', css_class='btn-primary')
        )

    class Meta:
        model = CLIENT

        exclude = ['author']

