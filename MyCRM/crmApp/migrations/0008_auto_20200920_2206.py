# Generated by Django 2.2.12 on 2020-09-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0007_aliproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliproducts',
            name='coupon_end_date',
            field=models.DateTimeField(blank=True, verbose_name='Coupon end date, GMT+8'),
        ),
        migrations.AlterField(
            model_name='aliproducts',
            name='coupon_start_date',
            field=models.DateTimeField(blank=True, verbose_name='Coupon start date, GMT+8'),
        ),
        migrations.AlterField(
            model_name='aliproducts',
            name='group_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='aliproducts',
            name='ws_display',
            field=models.CharField(blank=True, max_length=8, verbose_name='product offline reason'),
        ),
        migrations.AlterField(
            model_name='aliproducts',
            name='ws_offline_date',
            field=models.DateTimeField(blank=True, verbose_name='product offline time'),
        ),
    ]