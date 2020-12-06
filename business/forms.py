from django import forms
from .models import Business_News


class NewNewsForm(forms.ModelForm):
    class Meta:
        model = Business_News
        fields = '__all__'

