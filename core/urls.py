from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.home, name="home"),
]
