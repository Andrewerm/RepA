from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def users(request, month, year):
    return render(request, 'home.html', {month: month})