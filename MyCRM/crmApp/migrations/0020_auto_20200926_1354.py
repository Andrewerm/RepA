# Generated by Django 2.2.12 on 2020-09-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0019_auto_20200926_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliordersproductlist',
            name='send_goods_time',
            field=models.DateTimeField(null=True, verbose_name='Last delivery time'),
        ),
    ]
