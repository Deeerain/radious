from django.contrib import admin
from .models import Radio, Ganre, Feedback


@admin.register(Radio)
class RadioAdmin(admin.ModelAdmin):
    list_display = ('name', 'stream_url', 'slug', 'visible', 'created')
    list_editable = ('visible',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('visible', 'created')


@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rating', 'created')
    list_filter = ('created', 'rating')
