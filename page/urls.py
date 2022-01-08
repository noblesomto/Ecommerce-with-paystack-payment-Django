from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('page/product-details/<str:id>',
         views.product_details, name='product-details'),
    path('page/add_cart', views.add_cart, name="add_cart"),
    path('page/cart', views.cart, name="cart"),
    path('page/checkout', views.checkout, name="checkout"),
    path('page/verify/<str:id>', views.verify, name="verify"),
    path('page/order', views.order, name="order"),
    path('page/search', views.search, name="search"),
    path('page/payment-success', views.payment_success, name="payment-success"),
]
