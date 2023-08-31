from multiprocessing import context
from django.shortcuts import render, redirect
from watch.models import Contact
from .models import *
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
from .models import AboutUs
import os

config = {
  "apiKey": "AIzaSyBQ9iusYhHbIQrFk4E5jfhB3jmNwW5gGiQ",
  "authDomain": "stallion-1.firebaseapp.com",
  "projectId": "stallion-1",
  "storageBucket": "stallion-1.appspot.com",
  "messagingSenderId": "817196150899",
  "appId": "1:817196150899:web:276b26e577051e0819fa06",
  "measurementId": "G-DX54NG74X7",
  "databaseURL": "https://<stallion-1>.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

#About us page 


def about_us(request):
    about = AboutUs.objects.first()
    return render(request, 'about_us.html', {'about': about})
def about(request):
        return render(request, 'about.html')
# Create your views here.
# for add customers in admin 
def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Check if the 'name' field is present and not empty
        if name:
            emp = Contact(
                name=name,
                lastname=lastname,
                email=email,
                subject=subject,
                message=message
            )
            emp.save()
            return redirect('home')
        else:
            # Handle error when 'name' field is empty
            context = {
                'error_message': 'Name field is required.',
            }
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
# End add customers
def index(request):
    product=Product.objects.all()
    if request.method == 'POST':
        id=request.POST['product_id']
        product=Product.objects.get(id=id)
        print(product)
        try:
            customer = request.user.customer	
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)	

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('cart')
    context={'product':product}
    return render(request, 'index.html',context)

        



def addwish(request):
    return render(request, 'add-to-wishlist.html')

def cart(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    context = {'order':order}
    return render(request, 'cart.html',context)

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def men(request):
    product=Product.objects.all()
    if request.method == 'POST':
        id=request.POST['product_id']
        product=Product.objects.get(id=id)
        print(product)
        try:
            customer = request.user.customer	
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)	

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('cart')
    context={'product':product}
    return render(request, 'men.html',context)

def od(request):
    return render(request, 'order-complete.html')

def details(request):
    return render(request, 'product-detail.html')

def women(request):
    product=Product.objects.all()
    if request.method == 'POST':
        id=request.POST['product_id']
        product=Product.objects.get(id=id)
        print(product)
        try:
            customer = request.user.customer	
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)	

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('cart')
    context={'product':product}
    return render(request, 'women.html',context)


#firebase 



