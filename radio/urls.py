from django.urls import path

from . import views


app_name = 'radio'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('radio/', views.RadioListView.as_view(), name='radio-list'),
    path('radio/<slug:slug>/', views.RadioDetailView.as_view(),
         name='radio-detail'),
    path('ganre/', views.GanreListView.as_view(), name='ganre-list'),
    path('ganre/<slug:slug>/', views.RadioListByGanre.as_view(),
         name='ganre-detail'),
    path('favorite/', views.RadioListByFavorite.as_view(),
         name='favorite-list'),
]
