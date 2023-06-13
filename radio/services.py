from django.db import models
from django.contrib.sessions.backends.base import SessionBase

from radio import models as app_models


def stations_all(queryset: app_models.FeedbackQuerySet = None,
                 visible=True, **kwargs):
    '''Получает список станций и фильтрует по видимости'''
    queryset = queryset if not None else models.QuerySet(
        model=app_models.Radio)

    return queryset\
        .prefetch_related('feedbacks')\
        .annotate(rating=models.Avg('feedbacks__rating'))\
        .filter(visible=visible, **kwargs)


def station_by_slug(slug: str) -> app_models.Radio:
    '''Получает станцию по ее слагу'''
    return stations_all().get(slug=slug)


def stations_by_ganre(ganre_slug: str) -> app_models.RadioQuerySet:
    '''Получает станции по жанру'''
    return stations_all(ganre__slug=ganre_slug)


def stations_by_favorites(*station_ids) -> app_models.RadioQuerySet:
    '''Получает станции если они находятся в списке избранных'''
    return stations_all(pk__in=station_ids)


def station_add_to_favorite(station: app_models.Radio,
                            session: SessionBase) -> None:
    '''
    Добавляет станцию в список избранных

        Параметры:
            station: Модель станции
            session: Объект сессии
    '''

    session_favorites = session.get('stations_favorite', [])

    if station.pk not in session_favorites:
        session_favorites.append(station.pk)
        session.setdefault('stations_favorite', session_favorites)
        session.save()
