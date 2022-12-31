# Generated by Django 4.1.4 on 2022-12-27 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("masterclasses", "0010_alter_masterclass_mc_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="masterclass",
            name="mc_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="masterclasses.masterclasstype",
            ),
        ),
    ]
