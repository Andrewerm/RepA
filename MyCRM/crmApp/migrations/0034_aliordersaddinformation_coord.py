# Generated by Django 2.2.12 on 2020-11-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0033_auto_20201116_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliordersaddinformation',
            name='coord',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Координаты адреса покупателя'),
        ),
    ]
