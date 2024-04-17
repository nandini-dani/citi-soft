from django.shortcuts import render, redirect

from search_page.models import Address, Company, Product
from .forms import UploadCompanyForm, UploadLocationForm, UpdateProductForm

# Create your views here.


def company(request, id):
    companydetails = Company.objects.get(id=id)
    locations = Address.objects.filter(company_id=id)
    products = Product.objects.filter(company_id=id)
    is_vendor = True
    return render(
        request,
        "companydescription.html",
        {
            "company": companydetails,
            "locations": locations,
            "products": products,
            "is_vendor": is_vendor,
        },
    )


def companyedit(request, id):

    # locations = []
    companydetails = Company.objects.get(id=id)
    locations = Address.objects.filter(company_id=id)
    products = Product.objects.filter(company_id=id)
    return render(
        request,
        "companydescriptionedit.html",
        {
            "company": companydetails,
            "locations": locations,
            "products": products,
        },
    )


def editCompanyInfo(request, id):

    companydetails = Company.objects.get(id=id)
    compdata = Company.objects.filter(id=id).values()
    locations = Address.objects.filter(company_id=id)
    products = Product.objects.filter(company_id=id)
    # print(compdata)
    # form = form_class(request.POST or None)
    if request.method == "POST":
        print("inside form request")
        form = UploadCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            companydetails.name = form.cleaned_data["name"]
            companydetails.description = form.cleaned_data["description"]
            companydetails.company_url = form.cleaned_data["company_url"]
            if form.cleaned_data["company_image"] is None:
                # print("we dont have an image")
                # print(form.cleaned_data["company_image"])
                companydetails.company_image = compdata[0]["company_image"]
            else:
                companydetails.company_image = form.cleaned_data["company_image"]

            companydetails.save()

    else:
        form = UploadCompanyForm(initial=compdata[0])

    if request.method == "POST":
        print("inside form request 2")
        locationform = UploadLocationForm(request.POST)
        if locationform.is_valid():
            print("location is valid")
            # locations = form.cleaned_data["address"]
            # companydetails.description = form.cleaned_data["city"]
            # companydetails.company_url = form.cleaned_data["country"]
            # companydetails.company_image = form.cleaned_data["contact_number"]

            # companydetails.save()

    else:
        locationform = UploadLocationForm()
    return render(
        request,
        "infoeditpage.html",
        {
            "company": companydetails,
            "locations": locations,
            "products": products,
            "form": form,
            "locationform": locationform,
        },
    )


def productadd(request, id):
    print("inside product add")
    company = Company.objects.get(id=id)
    if request.method == "POST":
        print("inside post method")
        productAddForm = UpdateProductForm(request.POST, request.FILES)
        if productAddForm.is_valid():
            print("is valid")
            newProduct = Product()
            newProduct.name = productAddForm.cleaned_data["name"]
            newProduct.product_url = productAddForm.cleaned_data["product_url"]
            newProduct.business_areas = productAddForm.cleaned_data["business_areas"]
            newProduct.software_type = productAddForm.cleaned_data["software_type"]
            newProduct.product_doc = productAddForm.cleaned_data["product_doc"]
            newProduct.description = productAddForm.cleaned_data["description"]
            newProduct.product_type = productAddForm.cleaned_data["product_type"]
            newProduct.company = company
            newProduct.save()
            # productAddForm.save()
            url = f"/vendor/editCompanyInfo/{id}/"
            print(url)
            return redirect(url)

    else:
        productAddForm = UpdateProductForm()
        print("not under the post method for product add")

    return render(request, "product.html", {"productAddForm": productAddForm})


def addressadd(request, id):
    companydetails = Company.objects.get(id=id)
    locations = Address.objects.filter(company_id=id)
    print("in address add")
    if request.method == "POST":
        locationform = UploadLocationForm(request.POST)
        if locationform.is_valid():
            print("location form is valid")
            newaddress = Address()
            newaddress.city = locationform.cleaned_data["city"]
            newaddress.address = locationform.cleaned_data["address"]
            newaddress.country = locationform.cleaned_data["country"]
            newaddress.contact_number = locationform.cleaned_data["contact_number"]
            newaddress.company = companydetails

            newaddress.save()
    #             company
    # address
    # city
    # country
    # contact_number

    else:
        print("in else")
        locationform = UploadLocationForm()
    return render(request, "addressadd.html", {"locationform": locationform})


def productEdit(request, id):
    company = Company.objects.get(id=1)
    product = Product.objects.filter(id=id).values()
    newproduct = Product.objects.get(id=id)

    print("product is ", product)
    productAddForm = UpdateProductForm(initial=product[0])

    if request.method == "POST":

        print("inside product edit post")
        productAddForm = UpdateProductForm(request.POST, request.FILES)
        if productAddForm.is_valid():
            print("is valid productadd form KP")
            newproduct.name = productAddForm.cleaned_data["name"]
            newproduct.software_type = productAddForm.cleaned_data["software_type"]
            newproduct.description = productAddForm.cleaned_data["description"]
            newproduct.product_url = productAddForm.cleaned_data["product_url"]
            newproduct.product_doc = productAddForm.cleaned_data["product_doc"]
            newproduct.business_areas = productAddForm.cleaned_data["business_areas"]
            newproduct.product_type = productAddForm.cleaned_data["product_type"]
            newproduct.save()
            url = f"/vendor/editCompanyInfo/{company.id}/"
            print(url)
            return redirect(url)

    return render(
        request,
        "product.html",
        {"productAddForm": productAddForm, "product": product[0], "company": company},
    )
    # url = f"/vendor/editCompanyInfo/{id}/"
    # print(url)
    # return redirect(url)


def deleteProduct(request, id):

    print("in delete product")
    product = Product.objects.filter(id=id)
    print(product)
    product.delete()

    url = f"/vendor/editCompanyInfo/1/"
    print(url)
    return redirect(url)


def deleteLocation(request, id):

    print(" in delete location")
    location = Address.objects.filter(id=id)
    print(location)
    location.delete()
    url = f"/vendor/editCompanyInfo/1/"
    print(url)
    return redirect(url)


def locationEdit(request, id):
    print("in edit location")
    companydetails = Company.objects.get(id=1)

    location = Address.objects.filter(id=id).values()
    print(location)
    print("location is ", location[0])
    locationform = UploadLocationForm(initial=location[0])
    if request.method == "POST":
        locationform = UploadLocationForm(request.POST)
        if locationform.is_valid():
            print("location form edit is valid")
            newaddress = Address()
            newaddress.city = locationform.cleaned_data["city"]
            newaddress.address = locationform.cleaned_data["address"]
            newaddress.country = locationform.cleaned_data["country"]
            newaddress.contact_number = locationform.cleaned_data["contact_number"]
            newaddress.company = companydetails

            newaddress.save()

            url = f"/vendor/editCompanyInfo/1/"
            print(url)
            return redirect(url)

    return render(
        request,
        "addressadd.html",
        {"locationform": locationform, "location": location[0]},
    )
