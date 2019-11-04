from django import forms
from .models import ADSL_Document, ADSL_Abstract

class DocumentForm(forms.ModelForm):
    class Meta:
        model = ADSL_Document
        fields = ('title','description','document','uploaded_at')
class AbstractForm(forms.ModelForm):
    class Meta:
        model = ADSL_Abstract
        fields = ('title','description','date_submitted')
