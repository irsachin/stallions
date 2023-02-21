from django.contrib import admin

from watch.models import Product
from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)