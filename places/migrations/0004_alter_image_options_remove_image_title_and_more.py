# Generated by Django 4.2.20 on 2025-04-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_remove_place_first_image_remove_place_second_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.RemoveField(
            model_name='image',
            name='type_image',
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveBigIntegerField(db_index=True, default=0, verbose_name='Порядок'),
        ),
    ]
