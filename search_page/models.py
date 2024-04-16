from django.db import models
from django.core.validators import RegexValidator, URLValidator
from django.core.exceptions import ValidationError


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    date_of_establishement = models.DateField(("Date"), auto_now_add=False)
    vendor_id = models.CharField(max_length=6)
    phone_regex = RegexValidator(
        regex=r"^\+\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    contact_number = models.CharField(max_length=15, validators=[phone_regex])
    last_updated = models.DateField(("Date"), auto_now_add=True)
    company_url = models.URLField(max_length=50, validators=[URLValidator])
    company_image = models.ImageField(blank=True, upload_to="images/")
    employeecount = models.IntegerField()


product_type_choices = [
    ("choice1", "choice1"),
    ("choice2", "choice2"),
    ("choice3", "choice3"),
]


class Product(models.Model):
    company = models.ForeignKey(
        Company, related_name="companyId", on_delete=models.CASCADE, default=0
    )
    name = models.CharField(max_length=30)
    software_type = models.CharField(max_length=20)
    description = models.TextField()
    clients = models.CharField()
    cloud_based = models.BooleanField(default=False, null=True)
    cloud_native = models.BooleanField(default=False, null=True)
    product_url = models.URLField(max_length=50, validators=[URLValidator])
    product_doc = models.FileField(null=True, upload_to="documents/")
    business_areas = models.CharField(max_length=300)
    product_type = models.CharField(
        choices=product_type_choices, default="choice1", null=True
    )


class Address(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    address = models.TextField(unique=True)
    city = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=30, blank=False)
    phone_regex = RegexValidator(
        regex=r"^\+\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    contact_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        unique=True,
    )
