from django.http import HttpResponse
from django.shortcuts import render


def searchPage(request):
    return render(request, "index.html")
