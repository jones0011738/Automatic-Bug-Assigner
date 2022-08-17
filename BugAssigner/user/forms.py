from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, TextInput
from .models import Profile

class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'type':"username",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"}), label='Username:')
  password = forms.CharField(widget=forms.TextInput(attrs={'type':"password","minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"}), label='Password:')


class UserRegistrationForm(forms.ModelForm):
  password = CharField(label="Password", widget=forms.PasswordInput(attrs={
    'type':"password","minlength":"4",
    "class":"input-field",
    "autocomplete":"off",
    "required":"True"
  }))
  password2 = CharField(label="Repeat_Password", widget=forms.PasswordInput(attrs={
    'type':"password","minlength":"4",
    "class":"input-field",
    "autocomplete":"off",
    "required":"True"
  }))

  class Meta:
    model = User
    fields ={'username', 'first_name','last_name', 'email'}
    widgets = {
      'username': TextInput(attrs={"type":"username",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"

      }),
      'first_name': TextInput(attrs={"type":"username",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"

      }),
      'last_name': TextInput(attrs={"type":"username",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"

      }),
      'email': TextInput(attrs={"type":"email",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"

      }),
    }
  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError("Passwords do not match!")
    return cd['password2']

class ProfileEditForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['photo',]

class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


#     class Meta:
#         model = User
#         fields ={'username', 'first_name','last_name', 'email'}
#         widgets = {'username': TextInput(attrs={"type":"username",
#             "minlength":"4",
#             "class":"input-field",
#             "autocomplete":"off",
#             "required":"True"
#             }),
#             'first_name': TextInput(attrs={"type":"username",
#                 "minlength":"4",
#                 "class":"input-field",
#                 "autocomplete":"off",
#                 "required":"True"
#                 }),
#             'last_name': TextInput(attrs={"type":"username",
#                 "minlength":"4",
#                 "class":"input-field",
#                 "autocomplete":"off",
#                 "required":"True"
#                 }),
#             'email': TextInput(attrs={"type":"email",
#                 "minlength":"4",
#                 "class":"input-field",
#                 "autocomplete":"off",
#                 "required":"True"
#                 }),
#             }

