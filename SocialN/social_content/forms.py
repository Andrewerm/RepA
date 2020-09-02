from django import forms

from .models import Content

class ContentCreateForm(forms.ModelForm):
    class Meta:
        model=Content
        fields=('title', 'image', 'entry',)

class DeleteContentForms(forms.ModelForm):
    class Meta:
        model=Content
        fields=[]