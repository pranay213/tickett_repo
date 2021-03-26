from django import forms
from testapp.models import TicketSignup
from django.contrib.auth.models import User

class TicketSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
