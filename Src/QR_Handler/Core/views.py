from django.shortcuts import render

def Home(request):
    return render(request, "index.html")

def Scan(request):
    return render(request, "scan.html")