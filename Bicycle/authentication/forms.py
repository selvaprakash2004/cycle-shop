from django import forms

# Auth forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# The inbuilt User model
from django.contrib.auth.models import User
GENERAL_STYLE_ATTRS = {
    'class' :'form-control'
}

class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs=GENERAL_STYLE_ATTRS))
    email=forms.EmailField(widget=forms.EmailInput(attrs=GENERAL_STYLE_ATTRS))
    password1=forms.CharField(widget=forms.PasswordInput(attrs=GENERAL_STYLE_ATTRS))
    password2=forms.CharField(widget=forms.PasswordInput(attrs=GENERAL_STYLE_ATTRS))

    class meta:
        model=User
        fields=[
            'username','email','password1','password2'
        ]
    # Validation function for 'Email' Attribute
    def clean_email(self):
        #fetch the email from signup form
        submitted_email = self.cleaned_data.get('email')

    # Checking if the submitted email already belongs to a registered user
        if User.objects.filter(email=submitted_email).exists():
            raise forms.ValidationError('Email is associated with existing account!!!')
    # If mail is validated,return it to be stored
        return submitted_email 

class UserLoginForm(AuthenticationForm):
    username=forms.CharField(
        widget=forms.TextInput(attrs=GENERAL_STYLE_ATTRS)
    ) 
    password=forms.CharField(
        widget=forms.PasswordInput(attrs=GENERAL_STYLE_ATTRS)
    )      