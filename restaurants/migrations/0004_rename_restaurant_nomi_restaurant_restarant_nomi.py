# Generated by Django 4.0.3 on 2022-04-26 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_viloyat_davlat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_nomi',
            new_name='restarant_nomi',
        ),
    ]
