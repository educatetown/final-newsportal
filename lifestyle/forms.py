from django import forms
from .models import Lifestyle_News


class NewNewsForm(forms.ModelForm):
    class Meta:
        model = Lifestyle_News
        fields = '__all__'

