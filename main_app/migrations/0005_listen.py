# Generated by Django 4.1.3 on 2022-11-09 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_album_released'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('impressions', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.album')),
            ],
        ),
    ]