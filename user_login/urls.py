from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_registration, name="register"),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout')
    ]
