from django import forms
from uploads.core.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','description','author','class_div','rollno','name','document','uploaded_at', )
