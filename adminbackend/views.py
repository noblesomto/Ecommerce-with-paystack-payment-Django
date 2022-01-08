from django.core.checks import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User, UserManager, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature
from .models import Product, ProductImage
import random
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    posts = Product.objects.all()
    return render(request, 'frontend/index.html', {'posts': posts})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'backend/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(86400)
            request.session['username'] = user.username
            return redirect('/adminbackend/dashboard')
        else:
            messages.info(request, 'Credentials are invalid')
            return redirect('login')
    else:
        title = "Login"
        return render(request, 'backend/login.html', {'title': title})


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='/adminbackend/login')
def dashboard(request):
    title = "Admin Dashboard"
    return render(request, 'backend/index.html', {'title': title})


@login_required(login_url='/adminbackend/login')
def all_post(request):
    title = "All Posts"
    posts = Product.objects.all()
    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'backend/all-post.html', {'title': title, 'posts': page_obj})


@login_required(login_url='/adminbackend/login')
def new_post(request):
    if request.method == "POST" and request.FILES['product_picture']:
        product_title = request.POST['product_title']
        product_price = request.POST['product_price']
        product_picture = request.FILES['product_picture']
        product_category = request.POST['product_category']
        product_description = request.POST['product_description']
        prod_id = random.randint(0000, 9999)
        post = Product.objects.create(
            prod_id=prod_id, product_title=product_title, product_price=product_price, product_category=product_category,
            product_description=product_description, product_picture=product_picture)
        post.save()
        images = request.FILES.getlist('more_pictures')
        for image in images:
            photo = ProductImage.objects.create(
                image=image,
                prod_id=prod_id,
            )

        messages.info(
            request, 'Post was successful')
        return redirect('new_post')

    else:
        title = "New Product"
        return render(request, 'backend/new-post.html', {'title': title})


def post_details(request, id):
    posts = Product.objects.get(post_id=id)
    return render(request, 'frontend/post-details.html', {'posts': posts})


@login_required(login_url='/login')
def edit_post(request, id):
    prod_id = id
    posts = Product.objects.get(prod_id=id)
    if request.method == "POST":
        posts.product_title = request.POST['product_title']
        posts.product_price = request.POST['product_price']
        posts.product_picture = request.FILES['product_picture']
        posts.product_category = request.POST['product_category']
        posts.product_description = request.POST['product_description']
        posts.save()
        images = request.FILES.getlist('more_pictures')
        for image in images:
            photo = ProductImage.objects.create(
                image=image,
                prod_id=prod_id,
            )
        messages.info(
            request, 'Post was Edited successful')
        return redirect('edit_post', id=posts.prod_id)

    else:
        title = "Edit Product"
        return render(request, 'backend/edit-post.html', {'title': title, 'post': posts})


@login_required(login_url='/login')
def delete_post(request, id):
    posts = Product.objects.get(post_id=id)
    posts.delete()
    return redirect('index')
