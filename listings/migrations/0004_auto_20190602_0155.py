# Generated by Django 2.1.8 on 2019-06-01 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20190529_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='sqft',
            new_name='surface',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
    ]
