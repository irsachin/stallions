from multiprocessing import context
from django.shortcuts import render,redirect

from .models import *

# Create your views here.
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

        

def about(request):
        return render(request, 'about.html')

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