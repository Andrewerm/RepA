# Generated by Django 2.2.12 on 2020-12-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0046_auto_20201202_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliordersdetailedinformation',
            name='isPVZ',
            field=models.NullBooleanField(verbose_name='Есть ПВЗ в городе'),
        ),
    ]
