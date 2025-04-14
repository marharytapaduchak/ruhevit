from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # Додайте 'photo' до списку полів, якщо у вашій моделі користувача воно є
        fields = ['first_name', 'last_name', 'username', 'email', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишіть себе...'}),
        }
