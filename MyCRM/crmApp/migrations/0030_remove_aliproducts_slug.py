# Generated by Django 2.2.12 on 2020-10-06 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0029_aliproducts_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aliproducts',
            name='slug',
        ),
    ]