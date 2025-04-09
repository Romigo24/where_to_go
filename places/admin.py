from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('image_preview', )

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 150px; width: auto;" />', obj.image.url)
    
    image_preview.short_description = 'Превью'



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_image', 'image_preview')
    readonly_fields = ('image_preview', )

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 150px; width: auto;" />', obj.image.url)
    
    image_preview.short_description = 'Превью'