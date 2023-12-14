from django import forms
from messenger_app.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'image',
    )


class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'image')