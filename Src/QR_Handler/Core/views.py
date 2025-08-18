from django.shortcuts import render, redirect
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
from .models import QRImages
import io
from django.core.files.base import ContentFile

def Home(request):
    return render(request, "index.html")

def Scan(request):
    return render(request, "scan.html")

def ScanResult(request):
    if request.method == 'POST':
        file = request.FILES.get('image')
        image = Image.open(file)
        decoded = decode(image)
        type = ""
        data = ""
        for i in decoded:
            type = i.type
            data = i.data.decode("utf-8")
        return render (request, "scaned_code.html", {"type": type, "data": data})

def GenerateQRCode(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        qr = qrcode.QRCode(
            version=1.0,
            box_size=10,
            border=4
        )
        qr.add_data(code)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Save to model properly
        obj = QRImages()
        obj.image.save(f"{code}.png", ContentFile(buffer.getvalue()), save=True)

        return redirect(DisplayQRImage)
    return render(request, "generateQRCode.html")

def DisplayQRImage(request):
    QRImages.objects.exclude(id=QRImages.objects.last().id).delete()
    newImage = QRImages.objects.all()
    template = "displayQRImage.html"
    context = {
        "images": newImage
    }
    return render(request, template, context)