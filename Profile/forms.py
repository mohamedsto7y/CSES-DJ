from django import forms
from .models import *
class ProfileCreation(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your first name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your last name'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'enter your mail'}))
    class Meta:
        model=profile
        fields='__all__'
        exclude=['slug']