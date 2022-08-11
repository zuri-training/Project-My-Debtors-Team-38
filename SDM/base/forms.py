from email import message
from tkinter import Widget
from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    message = forms.Textarea()