from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_f, name='home'),
    path('about', views.about_f, name='about'),
]