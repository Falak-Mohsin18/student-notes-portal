from django import forms
from .models import Note
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'subject', 'pdf']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']