from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Ім'я користувача")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    ROLE_CHOICES = [
        ('волонтер', 'Волонтер'),
        ('військовий', 'Військовий'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES,
                             widget=forms.HiddenInput())
