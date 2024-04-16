from django.urls import path
from . import views
from .views import UserLoginView, EditProfileView

urlpatterns = [
    path("register/", UserLoginView.as_view(), name="register"),
    path("profile/", views.userProfile, name="userProfile"),
    path("editProfile/<int:pk>", EditProfileView.as_view(), name="editUserProfile"),
]
