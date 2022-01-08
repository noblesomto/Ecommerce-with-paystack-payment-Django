from django.core.checks import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User, UserManager, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Customer
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def register(request):
    if request.method == 'GET':
        title = "Register"
        return render(request, 'dashboard/register.html', {'title': title})
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        user_id = random.randint(0000, 9999)
        values = {
            'firstname': first_name,
            'lastname': last_name,
            'phone': phone,
            'email': email,
        }

        if password == password2:
            if Customer.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            elif Customer.objects.filter(phone=phone).exists():
                messages.info(request, 'Phone already exist')
                return redirect('register')
            else:
                password = make_password(password)
                user = Customer.objects.create(
                    user_id=user_id, first_name=first_name, last_name=last_name,
                    phone=phone, email=email, password=password)
                user.save()
                messages.info(request, 'Account Created, Please Login')
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register', {'values': values})


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            customer = None
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['user_id'] = customer.user_id
                request.session['email'] = customer.email
                return redirect("dashboard")
        else:
            messages.info(request, 'Email or Password is not correct')
            return redirect('login')
    else:
        title = "Login"
        return render(request, 'dashboard/login.html', {'title': title})


def logout(request):
    request.session.clear()
    return redirect('login')


def dashboard(request):
    title = "User Dashboard"
    user_id = request.session.get('user_id')
    return render(request, 'dashboard/index.html', {'title': title})
