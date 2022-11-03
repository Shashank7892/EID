from django import forms
from EID.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=['adhaar']
