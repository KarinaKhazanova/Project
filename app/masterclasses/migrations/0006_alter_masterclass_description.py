# Generated by Django 4.1.4 on 2022-12-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("masterclasses", "0005_masterclass_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="masterclass",
            name="description",
            field=models.TextField(max_length=120),
        ),
    ]