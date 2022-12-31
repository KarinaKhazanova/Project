# Generated by Django 4.1.4 on 2022-12-29 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclasses', '0021_masterclass_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclass',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]