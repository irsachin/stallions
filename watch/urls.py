from django.urls import path 
from . import views

# Create your models here.

urlpatterns = [
    path('index',views.index,name="Index"),
    path('',views.index,name="Index"),
    path('about',views.about,name="About"),
    path('addwish',views.addwish,name="wishlist"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="Checkout"),
    path('contact',views.contact,name="contact"),
    path('men',views.men,name="men"),
    path('ordercomplete',views.od,name="ordercomplete"),
    path('productdetails',views.details,name="productdetails"),
    path('women',views.women,name="Women")
]
