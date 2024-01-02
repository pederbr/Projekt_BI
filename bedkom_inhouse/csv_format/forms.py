from django import forms
from .models import opplastede_filer

class filForm(forms.ModelForm):
    class Meta:
        model = opplastede_filer
        fields = ["navn", "fil", "dato_bedpres", "lunsjpres"]
        widgets = {
            'dato_bedpres': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'} 
                ),
            'lunsjpres': forms.CheckboxInput()
        }