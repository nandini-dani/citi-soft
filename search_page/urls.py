from django.urls import path
from . import views
from .views import CompanyDetails

urlpatterns = [
    path("", views.searchPage, name="searchPage"),
    path("company/<int:pk>", CompanyDetails.as_view(), name="company-detail"),
]
