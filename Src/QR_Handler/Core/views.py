from django.shortcuts import render

def Home(request):
    return render(request, "index.html", {"text": "Hello world"})