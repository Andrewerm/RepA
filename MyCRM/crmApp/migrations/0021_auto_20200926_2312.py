# Generated by Django 2.2.12 on 2020-09-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0020_auto_20200926_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aliordersproductlist',
            old_name='main_order_id',
            new_name='main_order',
        ),
        migrations.RenameField(
            model_name='aliordersproductlist',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='aliorders',
            name='left_send_good_day',
            field=models.CharField(blank=True, default='', max_length=3, verbose_name='Remaining delivery time (days)'),
        ),
        migrations.AlterField(
            model_name='aliorders',
            name='left_send_good_hour',
            field=models.CharField(blank=True, default='', max_length=2, verbose_name='Remaining delivery time (hour)'),
        ),
        migrations.AlterField(
            model_name='aliorders',
            name='left_send_good_min',
            field=models.CharField(blank=True, default='', max_length=2, verbose_name='Remaining delivery time (minute)'),
        ),
    ]