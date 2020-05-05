from django.contrib import admin
from firstapp.models import PizzaShop, Pizza, Order
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pizza', 'name', 'date']

admin.site.register(Pizza)
admin.site.register(PizzaShop)
