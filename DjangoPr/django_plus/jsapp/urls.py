from django.urls import path
from .views import jsview



urlpatterns = [
    path('mine/', jsview),

]