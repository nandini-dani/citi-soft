from django.urls import path
from . import views
from .views import UserLoginView

urlpatterns = [
    path("register/", UserLoginView.as_view(), name="register"),
    path("profile/", views.userProfile, name="userProfile"),
]
