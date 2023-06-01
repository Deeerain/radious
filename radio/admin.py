from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Avg
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe

from .models import Radio, Ganre, Feedback


@admin.register(Radio)
class RadioAdmin(admin.ModelAdmin):
    list_display = ('draw_image', 'name', 'stream_url', 'slug',
                    'visible', 'created', 'get_rating')
    list_editable = ('visible',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('visible', 'created', 'ganre')
    search_fields = ('name', 'ganre')

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request)\
            .prefetch_related('feedbacks')\
            .annotate(rating=Avg('feedbacks__rating'))

    def get_rating(self, object):
        return object.rating

    def draw_image(self, object):
        if object.preview:
            tag = '<img src="%s" width="70" height="70" />' \
                % object.preview.url
            return mark_safe(tag)

    draw_image.description = 'Превью'


@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rating', 'created')
    list_filter = ('created', 'rating')
