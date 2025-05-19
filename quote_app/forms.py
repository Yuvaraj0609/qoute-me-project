from django import forms
from .models import ParcelQuote

class ParcelQuoteForm(forms.ModelForm):
    class Meta:
        model = ParcelQuote
        fields = '__all__'
