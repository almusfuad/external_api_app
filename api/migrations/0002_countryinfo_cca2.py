# Generated by Django 5.2 on 2025-05-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryinfo',
            name='cca2',
            field=models.CharField(default='', max_length=3),
        ),
    ]
