# Generated by Django 3.0 on 2022-06-11 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelTable(
            name='address',
            table=None,
        ),
        migrations.AlterModelTable(
            name='letting',
            table=None,
        ),
    ]
