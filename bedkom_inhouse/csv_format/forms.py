from django import forms
from .models import opplastede_filer
import pandas as pd

class filForm(forms.ModelForm):
    class Meta:
        model = opplastede_filer
        fields = ["navn", "fil", "dato_bedpres"]
        widgets = {
        'dato_bedpres': forms.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
        )
        }

