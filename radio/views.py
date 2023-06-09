from typing import Any, Dict
from django.shortcuts import redirect
from django.db.models.query import QuerySet
from django.db.models import Q, Avg
from django.http import HttpResponse
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic import ListView, DetailView, FormView

from radio.models import Radio, Ganre, Feedback
from radio.forms import FeedbackForm


class SearchMixin:
    search_fileds: list[str] = []
    search_name: str = 'search'

    def get_serch_value(self) -> str:
        return self.request.GET.get(self.search_name)

    def get_queryset(self) -> QuerySet[Any]:
        search_value = self.get_serch_value()

        if not search_value:
            return super().get_queryset()

        fr = [{v: search_value} for v in self.search_fileds]

        f = Q()
        for field in fr:
            f = f.__or__(Q(**field))

        return super().get_queryset().filter(f)


class HomeView(ListView):
    template_name = 'radio/home.html'
    model = Radio

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()\
            .prefetch_related('feedbacks')\
            .annotate(rating=Avg('feedbacks__rating'))


class RadioListView(SearchMixin, ListView):
    model = Radio
    search_fileds = ['name__icontains']

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(visible=True)


class RadioListByGanre(ListView):
    model = Radio

    def get_queryset(self) -> QuerySet[Any]:
        ganre_slug = self.kwargs.get('slug')
        return super().get_queryset().filter(ganre__slug=ganre_slug)


class RadioListByFavorite(RadioListView):
    def get_queryset(self) -> QuerySet[Any]:
        favorites = self.request.session.get('favorites')

        print(self.request.session.keys())

        if not favorites:
            return super().get_queryset().none()

        return super().get_queryset().filter(pk__in=favorites)


class RadioDetailView(DetailView, ModelFormMixin):
    model = Radio
    form_class = FeedbackForm
    success_url = "/"

    def form_valid(self, form: Any) -> HttpResponse:
        radio = self.get_object()
        form.radio = radio.pk
        return super().form_valid(form)

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()\
            .prefetch_related('feedbacks')\
            .annotate(rating=Avg('feedbacks__rating'))

    def post(self, response, slug):
        form = self.get_form()
        if form.is_valid():
            radio = self.get_object()
            Feedback.objects.get_or_create(**form.cleaned_data, radio=radio)
            return redirect(self.success_url)

        return self.form_invalid()


class GanreListView(ListView):
    model = Ganre
