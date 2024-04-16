from django import forms
from .models import UserProfile


class EditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "userImage",
            "f_name",
            "l_name",
            "contact_number",
            "email",
            "address",
        ]
        widgets = {
            "f_name": forms.TextInput(attrs={"class": "form-control"}),
            "l_name": forms.TextInput(attrs={"class": "form-control"}),
            "contact_number": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
        }
