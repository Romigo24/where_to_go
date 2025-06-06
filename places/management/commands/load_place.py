from urllib.parse import urlparse
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place


class Command(BaseCommand):
    help = 'Загружает одну локацию из JSON файла'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        json_url = options['json_url']
        self.stdout.write(f'Загружаем {json_url}...')

        response = requests.get(json_url)
        response.raise_for_status()
        place_raw = response.json()

        place, created = Place.objects.get_or_create(
            title=place_raw['title'],
            defaults={
                'short_description': place_raw['description_short'],
                'long_description': place_raw['description_long'],
                'lng': float(place_raw['coordinates']['lng']),
                'lat': float(place_raw['coordinates']['lat']),
            }
        )
        if not created:
            place.images.all().delete()        

        for order, img_url in enumerate(place_raw['imgs'], start=1):
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                img_name = urlparse(img_url).path.split('/')[-1]

                Image.objects.create(
                    place=place,
                    order=order,
                    image=ContentFile(img_response.content, name=img_name)
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Ошибка загрузки картинки {img_url}: {e}'))
            finally:
                img_response.close()

        self.stdout.write(self.style.SUCCESS(
            f'Успешно: {place.title} | Картинок: {len(place_raw["imgs"])}'
        ))