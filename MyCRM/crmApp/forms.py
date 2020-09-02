from django import forms
from .models import Brands, Stores, Catalog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BrandForm(forms.ModelForm):
    class Meta:
        model=Brands
        fields=['name', 'description', 'slug']

class SupplierForm(forms.Form):
    name=forms.CharField(max_length=20)
    slug=forms.SlugField()

class StoresForm(forms.ModelForm):
    class Meta:
        model=Stores
        fields=['catalog_item', 'quantity', 'wholesale_price', 'supplier', 'slug']

class CatalogForm(forms.ModelForm):
    class Meta:
        model=Catalog
        fields=['article', 'brand_name', 'model_name', 'model_series', 'slug']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=11, widget=forms.TextInput(attrs={'autofocus':True}))
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email']

