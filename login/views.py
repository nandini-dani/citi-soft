from django.shortcuts import render
from .models import UserProfile
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from search_page.models import Company
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from citisoft.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from .forms import EditForm


class UserLoginView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class EditProfileView(generic.UpdateView):
    model = UserProfile
    form_class = EditForm
    template_name = "editUserProfile.html"


def userProfile(request):
    userName = request.user.username
    user = User.objects.filter(username=userName)
    userData = UserProfile.objects.filter(user_id__in=user)
    companies = userData[0].liked_companies.all()
    likedCompany = companies.__len__

    if request.method == "POST" and request.POST.get("companyId"):
        companyId = request.POST.get("companyId")
        company = get_object_or_404(Company, pk=companyId)
        if company in userData[0].liked_companies.all():
            userData[0].liked_companies.remove(company)
        else:
            userData[0].liked_companies.add(company)
    elif request.method == "POST" and request.POST.get("notify"):
        companyId = request.POST.get("notify")
        company = get_object_or_404(Company, pk=companyId)
        print("hi", company)
        subject = "Enquiry sent to:" + company.name
        message = "Enquiry has been sent to the company"
        from_email = EMAIL_HOST_USER  # Your Gmail email address
        to_email = [
            userData[0].email,
        ]  # List of recipient email addresses
        # userData[0].f_name + " " + userData[0].l_name
        send_mail(subject, message, from_email, to_email)
        subjectCompany = "Enquiry From:" + userData[0].f_name + " " + userData[0].l_name
        messageCompany = "Enquiry has been received"
        from_emailCompany = EMAIL_HOST_USER  # Your Gmail email address
        to_emailCompany = [
            company.company_email,
        ]
        send_mail(subjectCompany, messageCompany, from_emailCompany, to_emailCompany)

    context = {
        "userData": userData,
        "companies": companies,
        "userProfile": userData[0],
        "likedCompany": likedCompany,
    }
    return render(request, "userProfile.html", context)
