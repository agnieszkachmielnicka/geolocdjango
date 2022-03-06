from django.urls import path

from . import views

# handler500 = 'rest_framework.exceptions.server_error'

urlpatterns = [
    path('koty', views.index, name='index'),
    path('api/', views.GeoLocationListView.as_view()),
    path('api/<path:ip_url>/', views.GeoLocationView.as_view())
]
