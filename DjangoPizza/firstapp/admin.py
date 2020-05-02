from django.contrib import admin
from firstapp.models import PizzaShop, Pizza
# Register your models here.

@admin.register(PizzaShop, Pizza)
class AuthorAdmin(admin.ModelAdmin):
    pass