from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def fruit(request):
    return render(request, "fruit.html")


def service(request):
    return render(request, "service.html")
