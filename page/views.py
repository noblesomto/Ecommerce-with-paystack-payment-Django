import json
from django.conf import settings
from django.shortcuts import render, redirect
from adminbackend.models import Product, ProductImage
from users.models import Customer, Order
from .middlewares.auth import auth_middleware
from pypaystack import Transaction, Customer, Plan
from django.http import JsonResponse
from django.core.paginator import Paginator
import random
import string

# Create your views here.


def index(request):
    title = "Home"
    posts = Product.objects.all()
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'frontend/index.html', {'title': title, 'posts': page_obj})


def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        title = "Search Result"
        posts = Product.objects.filter(
            product_title__icontains=search)
        paginator = Paginator(posts, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'frontend/search.html', {'title': title, 'posts': page_obj})


def add_cart(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('cart')
    else:
        return redirect('/')


def product_details(request, id):
    title = "Product Details"
    post = Product.objects.get(prod_id=id)
    images = ProductImage.objects.filter(prod_id=id)
    return render(request, 'frontend/product-details.html', {'title': title, 'post': post, 'images': images})


def cart(request):
    cart_product_id = list(request.session.get('cart').keys())
    cart_product = Product.get_products_by_id(cart_product_id)
    title = "View Cart"
    return render(request, 'frontend/cart.html', {'title': title, 'cart_product': cart_product})


def checkout(request):
    if request.method == "POST":
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        amount = request.POST.get("amount")
        customer = request.session.get("user_id")
        email = request.session.get("email")
        cart = request.session.get("cart")
        characters = string.ascii_uppercase + string.digits
        order_id = ''.join(random.choice(characters) for i in range(10))
        products = Product.get_products_by_id(list(cart.keys()))
        for product in products:
            order = Order(user_id=customer, order_id=order_id, prod_id=product.prod_id, product_title=product, product_price=product.product_price, address=address,
                          phone=phone, quantity=cart.get(str(product.prod_id)))
            order.save()

        return render(request, 'frontend/payment.html', {"email": email, 'phone': phone, 'amount': amount, 'ref': order_id, 'pk_public': settings.PAYSTACK_PUBLIC_KEY})

    else:
        cart_product_id = list(request.session.get('cart').keys())
        cart_product = Product.get_products_by_id(cart_product_id)
        title = "Check Out"
        return render(request, 'frontend/checkout.html', {'title': title, 'cart_product': cart_product})


@auth_middleware
def order(request):
    customer = request.session.get('user_id')
    order = Order.get_order_by_customer(customer)
    print(order)
    title = "Order Page"
    return render(request, 'frontend/orders.html', {'title': title, 'order': order})


def verify(request, id):
    transaction = Transaction(authorization_key=settings.PAYSTACK_SECRET_KEY)
    response = transaction.verify(id)
    status = response[3]["status"]
    if (status == "success"):
        order = Order.objects.get(order_id=id)
        order.status = True
        order.save()
        request.session['cart'] = {}
    data = JsonResponse(response, safe=False)
    return data


def payment_success(request):
    title = "Payment Success"
    return render(request, 'frontend/payment-success.html', {'title': title})
