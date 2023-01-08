from django import forms
from .models import Mystery, Answer
from django.contrib.auth.forms import UserCreationForm

class CreateMysteryForm(forms.ModelForm):
    class Meta:
        model = Mystery
        fields = ['title', 'description', 'clues', 'solution', 'tags']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']

class SignUpForm(UserCreationForm):
    # add any additional fields you want to include in the sign up form here
    pass

class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)