from django import forms
from .models import *
class ProfileCreation(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'