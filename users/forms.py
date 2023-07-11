from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from users.models import User


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Submit('submit', 'Submit', css_class='btn-primary')
        )


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(

            Submit('submit', 'Submit', css_class='btn-primary')
        )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
