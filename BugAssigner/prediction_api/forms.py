from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, TextInput, Textarea
from .models import Request

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = {'title', 'description'}
        widgets ={
                'title': TextInput(attrs={"type":"text",
                    "required":"True",
                    "class":"input-field"
                    }),
                 'description': Textarea(attrs={"type":"text",
                    "required":"True",
                    "rows":"3",
                    "class":"input-field"})
                 }



