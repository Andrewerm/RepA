from django import forms


class LoginForm(forms.Form):
    user=forms.CharField(max_length=12, label='Юзер')
    passw=forms.CharField(widget=forms.PasswordInput, label='пароль')

