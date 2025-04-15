from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True
    )
    short_description = models.TextField(
        blank=True,
        verbose_name='Короткое описание'
    )
    long_description = HTMLField(
        blank=True,
        verbose_name='Развернутое описание'
    )
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место',
        blank = True,
        null=True
        )
    order = models.PositiveBigIntegerField(
        default=0,
        db_index=True,
        verbose_name='Порядок',
    )
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title