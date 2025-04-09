from django import forms
from .models import RequestHistory


class RequestHistoryForm(forms.ModelForm):
    class Meta:
        model = RequestHistory
        fields = ['status', 'comment', 'photo']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишіть, що вже зроблено…'}),
        }
