# Generated by Django 2.2.12 on 2020-10-05 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0027_aliproducts_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aliproducts',
            name='slug',
        ),
    ]
