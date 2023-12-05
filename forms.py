from django import forms
from .models import buy

class mybuy(forms.ModelForm):
      class Meta:
            model=buy
            fields="__all__"
            