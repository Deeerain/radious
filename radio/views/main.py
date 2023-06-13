from django import http
from django.views import View
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from radio.views.mixins import SearchMixin
from radio import models as app_models
from radio.forms import FeedbackForm
from radio import services


class HomeView(generic.ListView):
    template_name = 'radio/home.html'
    model = app_models.Radio

    def get_queryset(self) -> app_models.RadioQuerySet:
        return services.stations_all(visible=True)


class RadioListView(SearchMixin, generic.ListView):
    model = app_models.Radio
    search_fileds = ['name__icontains']

    def get_queryset(self) -> app_models.RadioQuerySet:
        queryset = super().get_queryset()
        print("Main")

        return services.stations_all(queryset, visible=True)


class RadioListByGanreView(generic.ListView):
    model = app_models.Radio

    def get_queryset(self) -> app_models.RadioQuerySet:
        ganre_slug = self.kwargs.get('slug')
        return services.stations_by_ganre(ganre_slug)


class RadioListByFavoriteView(RadioListView):
    def get_queryset(self) -> app_models.RadioQuerySet:
        favorites = self.request.session.get('stations_favorite', [])

        return services.stations_by_favorites(*favorites)


@method_decorator(csrf_exempt, 'dispatch')
class AddStationToFavoriteView(View):
    def post(self, request: http.HttpRequest, slug):
        try:
            station = services.station_by_slug(slug)
            services.station_add_to_favorite(station, request.session)
            return http.HttpResponse('', status=200)

        except app_models.Radio.DoesNotExist:
            return http.HttpResponse('', status=404)


class RadioDetailView(generic.DetailView, generic.edit.ModelFormMixin):
    model = app_models.Radio
    form_class = FeedbackForm
    success_url = "/"

    def form_valid(self, form: FeedbackForm) -> http.HttpResponse:
        radio = self.get_object()
        form.radio = radio.pk
        return super().form_valid(form)

    def get_queryset(self) -> app_models.RadioQuerySet:
        return services.stations_all()

    def get_success_url(self) -> str:
        return self.request.headers.get('Referer') or self.success_url

    def post(self, *args, **kwargs) -> http.HttpResponse:
        form = self.get_form()
        if form.is_valid():
            radio = self.get_object()
            app_models.Feedback.objects.get_or_create(**form.cleaned_data,
                                                      radio=radio)
            return http.HttpResponseRedirect(self.get_success_url())

        return self.form_invalid()


class GanreListView(generic.ListView):
    model = app_models.Ganre
