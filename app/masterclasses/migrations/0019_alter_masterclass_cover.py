# Generated by Django 4.1.4 on 2022-12-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclasses', '0018_alter_masterclass_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclass',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
