from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    date_of_establishement = models.DateField(("Date"), auto_now_add=False)
    vendor_id = models.CharField(max_length=6)
    contact_number = models.CharField(max_length=15)
    last_updated = models.DateField(("Date"), auto_now_add=True)
    company_url = models.URLField(max_length=50)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=30)
    software_type = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    clients = models.CharField()
    cloud_based = models.BooleanField(default=False)
    cloud_native = models.BooleanField(default=False)


class Address(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    address = models.TextField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=15)
