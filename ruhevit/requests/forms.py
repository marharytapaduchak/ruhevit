from django import forms
from .models import *

class RequestHistoryForm(forms.ModelForm):
    class Meta:
        model = RequestHistory
        fields = ['status', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишіть, що вже зроблено...'}),
        }


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'description',
                'priority', 'location', 'type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
