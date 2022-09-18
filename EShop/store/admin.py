from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.cart import Cart
from .models.profile_image import ProfileImage
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['category', 'name', 'price']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['f_name','l_name','phone','email','password']


class AdminCart(admin.ModelAdmin):
    list_display = ['name','price','quantity','image']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order)
admin.site.register(ProfileImage)
admin.site.register(Cart, AdminCart)

