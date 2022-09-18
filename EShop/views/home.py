# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password, check_password
# from store.models.product import Product
# from store.models.category import Category
# from store.models.customer import Customer
# from django.views import View
#
#
# # Create your views here.
#
#
# def Index(request):
#     products = None
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_category_id(categoryID)
#     else:
#         products = Product.get_all_products()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print('Your email :: ',request.session.get('email'))
#     return render(request, 'store/index.html', data)
#
# # def regis_user(request):
# #
# #     post_data = request.POST
# #     f_name = post_data.get('f_name')
# #     l_name = post_data.get('l_name')
# #     phone = post_data.get('phone')
# #     email = post_data.get('email')
# #     password = post_data.get('password')
# #
# #     # Validation
# #     value = {
# #         'f_name': f_name,
# #         'l_name': l_name,
# #         'phone': phone,
# #         'email': email
# #     }
# #     error_message = None
# #
# #     # objects create
# #     customer = Customer(f_name=f_name, l_name=l_name, phone=phone, email=email, password=password)
# #
# #     error_message = validate_customer(customer)
# #     # Saving data
# #     if not error_message:
# #         customer.password = make_password(customer.password)
# #         # customer.save()
# #         customer.regis()            # regis is the method which is define in customer module
# #
# #         return redirect('products')
# #
# #     else:
# #         data = {
# #             'error': error_message,
# #             'values':value
# #         }
# #
# #         return render(request, 'store/register.html',data)
#
#
# # def Register(request):
# #     if request.method == 'GET':
# #         return render(request,'store/register.html')
# #     else:
# #         return  regis_user(request)
#
#
# # def login(request):
# #     if request.method == 'GET':
# #         return render(request,'store/login.html')
# #     else:
# #         email = request.POST.get('email')
# #         password = request.POST.get('password')
# #         customer = Customer.get_customer_by_email(email)
# #         error_message = None
# #         if customer:
# #             val = check_password(password,customer.password)
# #             if val:
# #                 return redirect('products')
# #             else:
# #                 error_message = 'Email or Password is invalid!!'
# #
# #         else:
# #             error_message = 'Email or Password is invalid!!'
# #         return render(request, 'store/login.html', {'error':error_message})
