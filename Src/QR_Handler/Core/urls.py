from django.urls import path
from .views import Home, Scan, ScanResult
urlpatterns = [
    path("", Home, name="home"),
    path("scan", Scan,name="scan"),
    path("qr-results", ScanResult, name="scan_result")
]