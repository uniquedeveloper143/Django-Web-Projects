from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.address import Address
from django.views import View
from store.middlewares.auth import auth_middleware
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

class Index(View):

    def post(self, request):
        p_id = request.POST.get('p_id')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            qty = cart.get(p_id)
            if qty:
                if remove:
                    if qty<=1:
                        cart.pop(p_id)
                    else:
                        cart[p_id] = qty-1
                else:
                    cart[p_id] = qty + 1
            else:
                cart[p_id] = 1
        else:
            cart = {}
            cart[p_id] = 1
        request.session['cart'] = cart
        print('cart :: ', request.session['cart'])
        return redirect('products')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        print(categoryID)
        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'store/index.html', data)

# def Index(request):
#     products = None
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_category_id(categoryID)
#     else:
#         products = Product.get_all_products()
#     data ={}
#     data['products'] = products
#     data['categories'] = categories
#
#     return render(request, 'store/index.html',data)


# def regis_user(request):
#
#     post_data = request.POST
#     f_name = post_data.get('f_name')
#     l_name = post_data.get('l_name')
#     phone = post_data.get('phone')
#     email = post_data.get('email')
#     password = post_data.get('password')
#
#     # Validation
#     value = {
#         'f_name': f_name,
#         'l_name': l_name,
#         'phone': phone,
#         'email': email
#     }
#     error_message = None
#
#     # objects create
#     customer = Customer(f_name=f_name, l_name=l_name, phone=phone, email=email, password=password)
#
#     error_message = validate_customer(customer)
#     # Saving data
#     if not error_message:
#         customer.password = make_password(customer.password)
#         # customer.save()
#         customer.regis()            # regis is the method which is define in customer module
#
#         return redirect('products')
#
#     else:
#         data = {
#             'error': error_message,
#             'values':value
#         }
#
#         return render(request, 'store/register.html',data)


class Register(View):
    def get(self, request):
        return render(request,'store/register.html')

    def post(self, request):
        post_data = request.POST
        f_name = post_data.get('f_name')
        l_name = post_data.get('l_name')
        phone = post_data.get('phone')
        email = post_data.get('email')
        password = post_data.get('password')

        # Validation
        value = {
            'f_name': f_name,
            'l_name': l_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        # objects create
        customer = Customer(f_name=f_name, l_name=l_name, phone=phone, email=email, password=password)

        error_message = self.validate_customer(customer)
        # Saving data
        if not error_message:
            customer.password = make_password(customer.password)
            # customer.save()
            customer.regis()  # regis is the method which is define in customer module

            return redirect('login')

        else:
            data = {
                'error': error_message,
                'values': value
            }

            return render(request, 'store/register.html', data)

    def validate_customer(self, customer):
        error_message = None
        if (not customer.f_name):
            error_message = "First name is required!!"
        elif len(customer.f_name) < 4:
            error_message = "First name must be 4 char or long!!"

        elif (not customer.l_name):
            error_message = "Last name is required!!"
        elif len(customer.l_name) < 4:
            error_message = "Last name must be 4 char or long!!"

        elif (not customer.phone):
            error_message = "Phone number is required!!"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 10 digit or long!!"

        elif (not customer.email):
            error_message = "Email ID is required!!"

        elif (not customer.password):
            error_message = "Password is required!!"
        elif len(customer.password) < 8:
            error_message = "Password must be 8 char or long!!"
        elif customer.isExists():
            error_message = 'Your Email ID is already Registered!!'
        return error_message

    # class Register(View):
    #     def get(self, request):
    #         return render(request, 'store/register.html')
    #
    #     def post(self, request):
    #         return regis_user(request)

# def Register(request):
#     if request.method == 'GET':
#         return render(request,'store/register.html')
#     else:
#         return  regis_user(request)


class Login(View):
    # return_url = None
    def get(self, request):
        # Login.return_url = request.GET.get('return_url')
        return render(request, 'store/login.html')

    def post(self, request):
        if request.method == 'GET':
            return render(request, 'store/login.html')
        else:
            email = request.POST.get('email')
            password = request.POST.get('password')
            customer = Customer.get_customer_by_email(email)
            error_message = None
            if customer:
                val = check_password(password, customer.password)
                if val:
                    request.session['customer'] = customer.id
                    return redirect('products')
                    # if Login.return_url:
                    #     return HttpResponseRedirect(Login.return_url)
                    # else:
                    #     Login.return_url = None
                    #     return redirect('products')
                else:
                    error_message = 'Email or Password is invalid!!'

            else:
                error_message = 'Email or Password is invalid!!'
            return render(request, 'store/login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')


class Cart(View):

    def get(self, request):
        customer = request.session.get('customer')
        add = Address.objects.filter(customer_id=customer)
        all_id=None
        if all_id == None:
            all_id = []
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        else:
            all_id = list(request.session.get('cart').keys())

        products = Product.get_products_by_id(all_id)
        print(products)

        return render(request, 'store/cart.html',{'products':products, 'add':add})



from random import randrange


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address,phone,customer,cart,products)
        order_id_ran = randrange(1,999)
        for product in products:
            order = Order(
                customer = Customer(id = customer),
                order_id = "ORD"+str(order_id_ran),
                product = product,
                price = product.price,
                address = address,
                phone = phone,
                quantity = cart.get(str(product.id))
            )

            order.place_order()
        request.session['cart'] = {}
        return redirect('cart')


class OrderPlace(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        return  render(request, 'store/orders.html',{'orders':orders})


def address(request):
    return render(request,'store/address.html')

def change_password(request):
    return render(request,'store/change_password.html')

def profile(request):
    customer = Customer.objects.filter(id=request.session['customer'])

    post_data = request.POST
    f_name = post_data.get('f_name')
    l_name = post_data.get('l_name')
    email = post_data.get('email')

    # Validation
    # new_id = request.session['customer']
    # Customer.objects.filter(id=new_id).update(f_name=f_name)
    # return HttpResponse("Done")

    return render(request,'store/profile.html',{'customer':customer})


def update_profile(request):
    post_data = request.POST
    f_name = post_data.get('f_name')
    l_name = post_data.get('l_name')
    email = post_data.get('email')

    # Validation
    new_id = request.session['customer']
    Customer.objects.filter(id=new_id).update(f_name=f_name,l_name=l_name,email=email)
    # return HttpResponse("Done")

    return redirect('profile')


class UpdatePass(View):
    def get(self, request):
        return render(request,'store/register.html')

    def post(self, request):
        post_data = request.POST
        old_pass = post_data.get('old_pass')
        new_pass = post_data.get('new_pass')
        c_pass = post_data.get('c_pass')

        # Validation
        error_message = None
        new_p = make_password(new_pass)
        # objects create
        customer = Customer.objects.get(id=request.session['customer'])

        # print(customer.password)
        # print(check_password(old_pass, customer.password))
        # Saving data

        if (not old_pass):
            error_message = "Old Password is required!!"
        if len(old_pass) < 8:
            error_message = "Old Password must be 8 char or long!!"

        if (not new_pass):
            error_message = "New Password is required!!"
        if len(new_pass) < 8:
            error_message = "New Password must be 8 char or long!!"

        if (not c_pass):
            error_message = "Confirm Password is required!!"
        if not c_pass==new_pass:
            error_message = "Password Does not match!!"
        if not check_password(old_pass, customer.password):
            error_message = "Old Password  is not valid!!"
        if not error_message:
            Customer.objects.filter(id=customer.id).update(password=new_p)
            return redirect('products')

        else:
            data = {
                'error': error_message,
            }

            return render(request, 'store/change_password.html', data)


def add_address(request):
    post_data = request.POST
    address = post_data.get('address')
    customer = request.session.get('customer')
    add = Address(address=address,customer_id=customer)
    add.save()
    return render(request,'store/index.html')

def view_add(request):
    customer = request.session.get('customer')
    add = Address.objects.filter(customer_id=customer)
    return render(request,'store/view.html',{'add':add})


def delete_add(request,eid):
    add = Address.objects.get(id=eid)
    add.delete()
    return redirect("view_address")

def edit_add(request,eid):
    add = Address.objects.get(id=eid)
    return render(request,'store/edit_address.html',{'add':add})

def edit_data_add(request,eid):
    add = request.POST.get('address')
    old_add = Address.objects.get(id=eid)
    Address.objects.filter(id=eid).update(address=add)
    return redirect('view_address')



# def login(request):
#     if request.method == 'GET':
#         return render(request,'store/login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             val = check_password(password,customer.password)
#             if val:
#                 return redirect('products')
#             else:
#                 error_message = 'Email or Password is invalid!!'
#
#         else:
#             error_message = 'Email or Password is invalid!!'
#         return render(request, 'store/login.html', {'error':error_message})
