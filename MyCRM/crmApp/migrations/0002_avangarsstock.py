# Generated by Django 2.2.17 on 2020-12-30 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvangarsStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
            ],
        ),
    ]
