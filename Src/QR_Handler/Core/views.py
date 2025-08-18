from django.shortcuts import render, redirect
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
from .models import QRImages
import io
from django.core.files.base import ContentFile
import cv2
import time

decodeText = ""

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

def LiveScan(request):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return render(request, "liveScan.html", {"error": "Camera not available"})

    capturedImage = "image.jpg"
    startTime = time.time()
    frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Laptop Camera", frame)

        # Close after 10 seconds
        if time.time() - startTime >= 10:
            cv2.imwrite(capturedImage, frame)
            break

        # Required to keep imshow window responsive
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Make sure an image was captured
    if frame is None:
        return render(request, "liveScan.html", {"error": "No frame captured"})

    # Decode QR code
    image = Image.open(capturedImage)
    decoded = decode(image)

    type = ""
    data = ""
    for i in decoded:
        type = i.type
        data = i.data.decode("utf-8")

    return render(request, "liveScan.html", {"type": type, "data": data})