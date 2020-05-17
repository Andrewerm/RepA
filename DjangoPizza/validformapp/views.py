from django.shortcuts import render
from . import forms
from .models import Phonebook

# Create your views here.

def form_page(request):
    firstRec=Phonebook.objects.all()
    if len(firstRec)>0:
        form=forms.NameForm(initial=firstRec[0])
        if request.method=='POST':
            form=forms.NameForm(request.POST)
            if form.is_valid():
                firstRec[0]['name']=form.cleaned_data['name']
                firstRec[0]['email']=form.cleaned_data['email']
                firstRec[0]['description']=form.cleaned_data['description']
    else:
        pass
    return render(request, 'validformapp/form_page.html', {'form':form})