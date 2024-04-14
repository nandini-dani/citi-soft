from django.contrib import admin
from .models import Product, Company, Address

# Register your models here.

admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Address)
