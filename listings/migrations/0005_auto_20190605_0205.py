# Generated by Django 2.1.8 on 2019-06-05 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20190602_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(blank=True, choices=[('Rent', 'Louer'), ('Buy', 'Vendre')], default='Buy', max_length=55),
        ),
    ]
