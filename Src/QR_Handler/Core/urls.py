from django.urls import path
from .views import Home, Scan, ScanResult, GenerateQRCode, DisplayQRImage, LiveScan
urlpatterns = [
    path("", Home, name="home"),
    path("scan", Scan,name="scan"),
    path("qr-results", ScanResult, name="scan_result"),
    path("generate-code", GenerateQRCode, name="generateQRCode"),
    path('display-qr-image', DisplayQRImage, name="displayQRImage"),
    path("live-scan-qr-code", LiveScan, name="liveScan")
]