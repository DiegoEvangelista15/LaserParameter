# Generated by Django 4.1.3 on 2022-12-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_parameter_piercing_gas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='potencia',
            field=models.FloatField(),
        ),
    ]
