from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower()!='a':
        raise forms.ValidationError('Make needs ta start a')

class NameForm(forms.Form):
    name=forms.CharField(validators=[check_for_a])
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter email again')
    text=forms.CharField(widget=forms.Textarea,
                         validators=[validators.MaxLengthValidator(5)])
    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data['email']
        vmail=cleaned_data['verify_email']
        if email!=vmail:
            raise forms.ValidationError('Make sure email match')
        return cleaned_data

