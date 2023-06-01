from datetime import timedelta

from django.utils import timezone
from django import template
from django.db.models import QuerySet


register = template.Library()


@register.filter(name='newest')
def newest_filter(queryset: QuerySet, count: int = 5):
    now = timezone.now()

    return queryset\
        .filter(created__gte=(now - timedelta(days=7)).date())[:count]


@register.filter(name='popular')
def popular_filter(queryset: QuerySet, count: int = 5):
    return queryset.filter(rating=5)
