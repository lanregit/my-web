from django import forms
from django.core import validators



class Contact(forms.Form):
    f_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name (Required)'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email (Required)'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}))

# class Contact2(forms.Form):
#     f_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name2 (Required)'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email2 (Required)'}))
#     comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message2'}))


class NewsLetter(forms.Form):
    ur_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email', 'color':'white'}))
