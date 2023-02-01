from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    message = forms.CharField(widget= forms.Textarea, max_length=2000)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {k:"" for k in fields}