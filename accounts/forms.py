from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailField, EmailInput, PasswordInput


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        widgets = {
            'username': TextInput(attrs={'placeholder': 'enter your username here...'}),
            'password': PasswordInput()
        }


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'enter your first name here...'}),
            'last_name': TextInput(attrs={'placeholder': 'enter your last name here...'}),
            'email': EmailInput(attrs={'placeholder': 'username@example.com'})
        }
