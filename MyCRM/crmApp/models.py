from djmoney.models.fields import MoneyField
from django.db import models
from django.urls import reverse

# Сущность Бренды
class Brands(models.Model):
    name=models.CharField(max_length=20) # поле наимнование бренда
    description=models.TextField(max_length=200, blank=True)
    slug=models.SlugField(unique=True) # путь к страничке бренда
    def __str__(self):
         return self.name
    def get_absolute_url(self):
        return reverse('crm:brand_details', args=[self.slug])
    class Meta:
        verbose_name='Бренд'
        verbose_name_plural='Бренды'

# Сущность Серии, к которым относится модель
class Series(models.Model):
    name=models.CharField(max_length=20) # Наименование серии
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Серия'
        verbose_name_plural='Серии'

# Сущность Каталог моделей какие вообще бывают в природе
class Catalog(models.Model):
    article=models.CharField(max_length=7, unique=True, help_text='артикул товара') # артикул, уникальное поле
    brand_name=models.ForeignKey(Brands, on_delete=models.DO_NOTHING,
                                 related_name='catalog_items') # связь с сущностью Бренды
    model_name=models.CharField(max_length=20, help_text='модель') # Наименование модели
    model_series=models.ManyToManyField(Series, blank=True) # связь с сущностью Серии
    slug=models.SlugField(unique=True)
    def __str__(self):
         return self.brand_name.name+' '+self.model_name
    def get_absolute_url(self):
        return reverse('crm:model_details', args=[self.slug])
    class Meta:
        verbose_name='Модель'
        verbose_name_plural='Каталог моделей'


# Сущность поставщики
class Suppliers(models.Model):
    name=models.CharField(max_length=20, verbose_name='Наименование поставщика') # Наименование поставщика
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('crm:suppliers_details', args=[self.slug])
    class Meta:
        verbose_name='поставщик'
        verbose_name_plural='Поставщики'

# Сущность информация по остаткам и ценам на складах у поставщиков
class Stores(models.Model):
    catalog_item=models.ForeignKey(Catalog, related_name='item_of_store', on_delete=models.DO_NOTHING, verbose_name='Модель')
    quantity=models.IntegerField(blank=True, verbose_name='количество')
    wholesale_price=MoneyField(max_digits=14, decimal_places=2, default_currency='RUR', blank=True, verbose_name='оптовая цена')
    supplier=models.ForeignKey(Suppliers,on_delete=models.DO_NOTHING, related_name='items_of_supplier', verbose_name='поставщик')
    slug=models.SlugField(unique=True)
    def __str__(self):
         return self.supplier.name
    def get_absolute_url(self):
        return reverse('crm:store_item', args=[self.slug])
    class  Meta:
        verbose_name='Складской запас'
        verbose_name_plural='Складские запасы'


