from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("search_page.urls")),
    # path("user/", include("django.contrib.auth.urls")),
    path("user/", include("user_login.urls"))
]
