from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from search_page.models import Company


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    # liked_vendors = ArrayField(models.CharField(max_length=500), blank=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, unique=True)
    liked_companies = models.ManyToManyField(
        Company, related_name="liked_by", blank=True
    )

    def __str__(self):
        return self.user.username
