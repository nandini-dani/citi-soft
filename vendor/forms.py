from django.forms import ModelForm
from django import forms
from search_page.models import Address, Company, Product


class UploadCompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = (
            "name",
            "description",
            "company_url",
            "company_image",
            # "employeecount",
        )

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "company_url": forms.URLInput(attrs={"class": "form-control"}),
            "company_image": forms.FileInput(attrs={"class": "form-control"}),
        }


class UploadLocationForm(ModelForm):

    # address = forms.CharField(label="address", max_length=80, required=True)
    # city = forms.CharField(label="city", max_length=25, required=True)
    # country = forms.CharField(label="country", max_length=35, required=True)
    # contact_number = forms.CharField(
    #     label="contactnumber", max_length=10, required=True
    # )

    class Meta:
        model = Address
        fields = ("address", "city", "country", "contact_number")

        widgets = {
            "address": forms.TextInput(
                attrs={"class": "form-control", "label": "address", "required": "True"}
            ),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "contact_number": forms.TextInput(attrs={"class": "form-control"}),
        }


class UpdateProductForm(ModelForm):

    class Meta:
        model = Product
        fields = (
            "name",
            "product_url",
            "business_areas",
            "software_type",
            "product_type",
            "product_doc",
            "description",
        )

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "product_url": forms.TextInput(attrs={"class": "form-control"}),
            "business_areas": forms.TextInput(attrs={"class": "form-control"}),
            "software_type": forms.TextInput(attrs={"class": "form-control"}),
            "product_type": forms.Select(attrs={"class": "form-control"}),
            "product_doc": forms.FileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


#         name
# software_type
# description
# clients
# cloud_based
# cloud_native
# product_url
# product_doc
# business_areas
# product_type
