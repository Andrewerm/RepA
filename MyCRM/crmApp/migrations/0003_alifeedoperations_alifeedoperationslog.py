# Generated by Django 2.2.12 on 2021-02-08 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0002_auto_20210208_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliFeedOperations',
            fields=[
                ('jobID', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('timeOperation', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AliFeedoperationsLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_content_id', models.CharField(max_length=15)),
                ('item_execution_result', models.CharField(blank=True, default='', max_length=250)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmApp.AliFeedOperations')),
            ],
            options={
                'unique_together': {('job', 'item_content_id')},
            },
        ),
    ]
