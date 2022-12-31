# Generated by Django 4.1.4 on 2022-12-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("masterclasses", "0008_remove_masterclass_date_masterclassdate"),
    ]

    operations = [
        migrations.CreateModel(
            name="MasterclassType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=24)),
                ("description", models.CharField(max_length=24)),
            ],
        ),
        migrations.AddField(
            model_name="masterclass",
            name="mc_type",
            field=models.CharField(default="", max_length=2),
        ),
    ]
