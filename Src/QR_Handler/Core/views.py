from django.shortcuts import render
from pyzbar.pyzbar import decode
from PIL import Image

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
            print("Type: ", i.type)
            print("Data: ", i.data.decode("utf-8"))
            type = i.type
            data = i.data.decode("utf-8")
        return render (request, "scaned_code.html", {"type": type, "data": data})

