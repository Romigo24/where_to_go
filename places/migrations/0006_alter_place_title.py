# Generated by Django 4.2.20 on 2025-04-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
    ]
