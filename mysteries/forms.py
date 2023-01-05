from django import forms
from .models import Mystery

class CreateMysteryForm(forms.ModelForm):
    class Meta:
        model = Mystery
        fields = ['title', 'description']
