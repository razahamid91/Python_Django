from django  import forms
class ContactForm(forms.Form):
    name = forms.CharField(label= "your name", max_length=100)
    email = forms.CharField(label= "your Email address")
    subject = forms.CharField(label= "Subject", max_length=200)
    message = forms.CharField(label= "Message", widget=forms.Textarea)