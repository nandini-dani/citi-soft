from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Company


def searchPage(request):
    products = Product.objects.all()
    companies = Company.objects.all()
    resultCompanies = None
    resultCompaniesLength = 0
    if request.GET.get("searchQuery"):
        search = request.GET.get("searchQuery")
        resultCompanies = Company.objects.filter(name__icontains=search)
        resultCompanies.__len__()
        resultCompaniesLength = resultCompanies.__len__()
    context = {
        "companies": companies,
        "list": [1, 2, 3],
        "resultCompanies": resultCompanies,
        "resultCompaniesLength": resultCompaniesLength,
    }
    return render(request, "search_page.html", context)
