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


class OrderInfoForm(forms.Form):
    SOURCE_CITIES=(('selectTarifSaratov','Из Саратова'), ('selectTarifKazan', 'Из Казани'), ('selectTarifChelny', 'Из Н.Челнов'))
    recieverFIO=forms.CharField(label='ФИО получателя', max_length=30)
    selectPVZ=forms.ChoiceField(label='ПВЗ СДЭК получателя')
    selectShippingFrom=forms.ChoiceField(label='Город отправки', widget=forms.RadioSelect, choices=SOURCE_CITIES, initial=SOURCE_CITIES[0])
    selectTarifSaratov=forms.ChoiceField(label='Тариф СДЭК из Саратова')
    selectTarifKazan = forms.ChoiceField(label='Тариф СДЭК из Казани')
    selectTarifChelny = forms.ChoiceField(label='Тариф СДЭК из Н. Челнов')
    insurance=forms.IntegerField(label='Страховка груза (руб.):', required=False)


