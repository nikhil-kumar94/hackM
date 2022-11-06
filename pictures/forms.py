from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class PersonForm(ModelForm):
    class Meta:
        model=Person
        fields='__all__'
        exclude=['user','participant']

class MessageForm(ModelForm):
    class Meta:
        model=Person
        fields='__all__'
        
        
# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['name','username','email','password1','password2']