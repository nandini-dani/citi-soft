from django.shortcuts import render
from .models import Company, Product
from django.views import generic
from django.forms.models import model_to_dict
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from login.models import UserProfile


@login_required
def searchPage(request):
    companies = Company.objects.all()
    recCompanies = companies[:6]
    firstRecCompanies = recCompanies[: len(recCompanies) // 2]
    secondRecCompanies = recCompanies[len(recCompanies) // 2 :]
    resultCompanies = None
    resultCompaniesLength = 0
    user = User.objects.filter(username=request.user.username)
    userProfile = UserProfile.objects.filter(user_id__in=user)
    filterCloudCategory = [
        {"categoryId": "cloud_based", "categoryName": "Cloud Based", "checked": False},
        {
            "categoryId": "cloud_native",
            "categoryName": "Cloud Native",
            "checked": False,
        },
        {
            "categoryId": "cloud_enabled",
            "categoryName": "Cloud Enabled",
            "checked": False,
        },
    ]
    filterSoftwareType = [
        {
            "categoryName": "Alternative investment",
            "checked": False,
        },
        {
            "categoryName": "Data Management",
            "checked": False,
        },
        {
            "categoryName": "Data Transformation",
            "checked": False,
        },
        {
            "categoryName": "Enterprise Architecture",
            "checked": False,
        },
        {
            "categoryName": "Wealth Management",
            "checked": False,
        },
        {
            "categoryName": "Process Automation",
            "checked": False,
        },
    ]

    if request.GET.get("searchQuery"):
        search = request.GET.get("searchQuery")
        resultCompanies = Company.objects.filter(name__icontains=search)
        resultCompaniesLength = resultCompanies.__len__()
        print("***", resultCompaniesLength)
        if resultCompaniesLength <= 0:
            resultproducts = Product.objects.filter(
                Q(name__icontains=search) | Q(software_type__icontains=search)
            )
            resultproductsLength = resultproducts.__len__()
            print("***", resultproducts)
            if resultproductsLength > 0:
                resultCompanies = Company.objects.filter(
                    id__in=resultproducts.values_list("company_id", flat=True)
                ).distinct()
                resultCompaniesLength = resultCompanies.__len__()
        # Convert the serialized data to a list of dictionaries
        resultCompaniesList = [model_to_dict(item) for item in resultCompanies]
        for item in resultCompaniesList:
            item["date_of_establishement"] = item["date_of_establishement"].strftime(
                "%Y-%m-%d"
            )
        request.session["resultCompaniesList"] = list(resultCompaniesList)

    elif request.GET.get("category"):
        serializedQuerySet = request.session.get("resultCompaniesList", [])
        queryset = [Company(**item) for item in serializedQuerySet]
        resultCompanies = queryset
        categoryFetched = request.GET.getlist("category")
        value = True
        q_objects = Q()

        # Add each category as a separate condition to the Q object
        for category in categoryFetched:
            q_objects |= Q(**{category: value})
        # filter_args = {categoryFetched: value}
        # Retrieve related ChildModel objects for each ParentModel object in existing_queryset
        related_child_objects = Product.objects.filter(company_id__in=resultCompanies)
        print("nan2", related_child_objects)
        prod = related_child_objects.filter(q_objects)
        # resultCompanies = resultCompanies.filter(name__icontains=search)
        print("nan3", prod)
        resultCompanies = Company.objects.filter(
            id__in=prod.values_list("company_id", flat=True)
        ).distinct()
        resultCompaniesLength = resultCompanies.__len__()

        for category in filterCloudCategory:
            for check in categoryFetched:
                if category["categoryId"] == check:
                    category["checked"] = True
    if request.method == "POST":
        companyId = request.POST.get("companyId")
        company = get_object_or_404(Company, pk=companyId)
        if company in userProfile[0].liked_companies.all():
            userProfile[0].liked_companies.remove(company)
        else:
            userProfile[0].liked_companies.add(company)
    context = {
        "firstRecCompanies": firstRecCompanies,
        "secondRecCompanies": secondRecCompanies,
        "list": [1, 2, 3],
        "resultCompanies": resultCompanies,
        "resultCompaniesLength": resultCompaniesLength,
        "filterCloudCategory": filterCloudCategory,
        "filterSoftwareType": filterSoftwareType,
        "userProfile": userProfile[0],
    }
    return render(request, "search_page.html", context)


class CompanyDetails(generic.DetailView):
    model = Company
    template_name = "company_detail.html"
