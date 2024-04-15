from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login

import logging
User = get_user_model()
logger = logging.getLogger('django')

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        try:
            user = User.objects.get(username=username)
            #  Check the password is the reverse of the username
            if check_password(password, user.password):
                login(request, user)
                context = {'loginSuccess': True, 'errorMessage': ''}
                request.session['username'] = user.name
                return render(request, "search_page.html", context)
            else:
                # No? return None - triggers default login failed
                context = {'loginSuccess': False, 'errorMessage': 'Invalid Credentials!'}
                return render(request, "login.html", context=context)
        except User.DoesNotExist:
        # No user was found, return None - triggers default login failed
            context = {'loginSuccess': False, 'errorMessage': 'Invalid User Name!'}
            return render(request, "login.html", context=context)
    else:
        return render(request, "login.html")

def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# Create your views here.
def user_registration(request, **extra_fields):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        recovery_email = request.POST.get("recovery_email", "")
        phone_number = request.POST.get("phone_number", "")
        user = User.objects.create_user(username = username , password = password , email = email, name = name,
                                        recovery_email = recovery_email, phone_number= phone_number)
        user.save()
        context = {'registrationSuccess': True}
        return render(request, "registration.html", context=context)
    else:
        return render(request, "registration.html")
    
def user_email_validation(request):
    if request.method == 'POST':
        email = request.POST.get("email", "")