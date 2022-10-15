from django.forms import ModelForm, Textarea
from django import forms
from .models import Contact


class ContactForm(ModelForm):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    # time = .  #DateTimeField(auto_now_add=True)

    # class Meta:
    #     model = Contact
    #     fields = ['first_name', 'last_name', 'email', 'message']
    #     widgets = {
    #         'message': Textarea(attrs={'placeholder': 'Ваше сообшение'})
    #     }
