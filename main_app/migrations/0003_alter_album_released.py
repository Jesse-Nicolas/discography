# Generated by Django 4.1.3 on 2022-11-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_album_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='released',
            field=models.CharField(max_length=4, verbose_name='date released'),
        ),
    ]
