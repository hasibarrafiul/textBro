from django import forms
from . import models


class textsForm(forms.ModelForm):
    class Meta:
        model = models.texts
        fields = ['text_link', 'text_password']

