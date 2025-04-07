from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Ім'я користувача")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
