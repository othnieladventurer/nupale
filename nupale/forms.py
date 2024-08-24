from django import forms
from django.forms import ModelForm, Form

from .models import *





class QuoteCreationForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"






class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
   
    message = forms.CharField(widget=forms.Textarea)






