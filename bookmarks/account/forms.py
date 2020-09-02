from django import forms


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password=forms.CharField(widget=forms.PasswordInput)