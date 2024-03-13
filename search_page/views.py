from django.http import HttpResponse
from django.shortcuts import render


def searchPage(request):
    context = {
        "list": [1, 2, 3],
    }
    return render(request, "search_page.html", context)
