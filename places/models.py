from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    short_description = models.TextField(
        blank=True,
        verbose_name='Короткое описание'
    )
    long_description = models.TextField(
        blank=True,
        verbose_name='Развернутое описание'
    )
    lng = models.FloatField(verbose_name='Долгота')
    lan = models.FloatField(verbose_name='Широта')
    
    def __str__(self):
        return self.title