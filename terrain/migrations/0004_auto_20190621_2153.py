# Generated by Django 2.1.8 on 2019-06-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrain', '0003_auto_20190602_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terrain',
            name='type',
            field=models.CharField(blank=True, choices=[('Commercial', 'Commercial'), ('Habitation', 'Habitation'), ('Agriculture', 'Agriculture'), ('Promotion immobilière', 'Promotion immobilière')], max_length=55),
        ),
    ]
