from django.urls import path
from .views import Home, Scan
urlpatterns = [
    path("", Home, name="home"),
    path("scan", Scan,name="scan")
]