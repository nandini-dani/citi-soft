from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("company/<id>/", views.company, name="company"),
    path("companyedit/<id>/", views.companyedit, name="company"),
    path("editCompanyInfo/<id>/", views.editCompanyInfo, name="infoedit"),
    path("productAdd/<id>/", views.productadd, name="productAdd"),
    path("addressAdd/<id>/", views.addressadd, name="addressAdd"),
    path("productEdit/<id>/", views.productEdit, name="productEdit"),
    path("deleteProduct/<id>/", views.deleteProduct, name="deleteProduct"),
    path("deleteLocation/<id>/", views.deleteLocation, name="deleteLocation"),
    path("locationEdit/<id>/", views.locationEdit, name="locationEdit"),
]
