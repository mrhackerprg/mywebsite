from django import forms
from .models import SendMessage

class Message(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = ["id" , "name" , "email" , "subject" , "message"]