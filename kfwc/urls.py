from django.urls import path

from . import views

urlpatterns = [
    path("", views.user_login, name="index"),
    path("home", views.home, name="home"),
]