from django.shortcuts import render

from django.template.response import TemplateResponse

def jsview(request):
    return TemplateResponse(request, 'jsapp/jsapp_index.html')
