# Generated by Django 2.2.17 on 2021-01-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0007_auto_20210109_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('count', models.SmallIntegerField()),
            ],
        ),
    ]
