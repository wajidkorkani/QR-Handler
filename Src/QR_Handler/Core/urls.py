from django.urls import path
from .views import Home, Scan, ScanResult, GenerateQRCode, DisplayQRImage
urlpatterns = [
    path("", Home, name="home"),
    path("scan", Scan,name="scan"),
    path("qr-results", ScanResult, name="scan_result"),
    path("generate-code", GenerateQRCode, name="generateQRCode"),
    path('display-qr-image', DisplayQRImage, name="displayQRImage")
]