from django.contrib import admin
from django.urls import path, include
import Core

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Core.urls"))
]
