from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name= models.CharField(max_length=30, verbose_name='Пиццерия')
    description= models.TextField(verbose_name='Описание')
    rating=models.FloatField(default=0, verbose_name='Рейтинг')
    url=models.URLField(verbose_name='Интернет адрес пиццерии')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Пиццерия'
        verbose_name_plural='Пиццерии'

class Pizza(models.Model):
    pizzashop=models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name=models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description=models.CharField(max_length=30, verbose_name='Краткое описание')
    price=models.IntegerField(default=0, verbose_name='Цена')
    photo=models.ImageField('Фото',upload_to='firstapp/photos',default='', blank=True)
    def __str__(self): return self.name
    class Meta:
        verbose_name='Пицца'
        verbose_name_plural='Пиццы'
        ordering=['name']
class Order(models.Model):
    pizza=models.ForeignKey(Pizza, verbose_name='Пицца', on_delete=models.CASCADE)
    name=models.CharField(max_length=30, verbose_name='Имя')
    phone=models.CharField(max_length=30, verbose_name='Телефон')
    date=models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    def __str__(self): return str(self.date)
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'
        ordering=['date']