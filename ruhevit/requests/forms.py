from django import forms
from .models import *

# class RequestHistoryForm(forms.ModelForm):
#     class Meta:
#         model = RequestHistory
#         fields = ['status', 'comment']
#         widgets = {
#             'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишіть, що вже зроблено...'}),
#         }


# class RequestForm(forms.ModelForm):
#     class Meta:
#         model = Request
#         fields = ['name', 'description',
#                 'priority', 'location', 'type']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }


class RequestHistoryForm(forms.ModelForm):
    class Meta:
        model = RequestHistory
        fields = ['status', 'comment']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишіть, що вже зроблено...'
            }),
        }


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'description', 'priority', 'location', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }