# Generated by Django 2.2.11 on 2020-03-26 11:08

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
