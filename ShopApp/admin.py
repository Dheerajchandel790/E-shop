from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (  'user','name', ) 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'p_name', 'category' , 'barnd','selling_price',  'discounted_price', 'discription', 'image' ) 

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'product',  'quantity') 

@admin.register(OrderPlaced)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'customer', 'product',  'quantity', 'cart', 'order_date' , 'status' ) 

# Register your models here.
