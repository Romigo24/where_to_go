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
    lat = models.FloatField(verbose_name='Широта')

    
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    TYPE_IMAGE = [
        ('first_image', 'Первая картинка'),
        ('second_image', 'Вторая картинка')
    ]

    title = models.CharField(max_length=100, verbose_name='Название картинки')
    type_image = models.CharField(max_length=50, choices=TYPE_IMAGE, verbose_name='Тип картинки')
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место',
        blank = True,
        null=True
        )

    def __str__(self):
        return self.title