# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from store.models.customer import Customer
# from django.views import View
#
#
# class Register(View):
#     def get(self, request):
#         return render(request, 'store/register.html')
#
#     def post(self, request):
#         post_data = request.POST
#         f_name = post_data.get('f_name')
#         l_name = post_data.get('l_name')
#         phone = post_data.get('phone')
#         email = post_data.get('email')
#         password = post_data.get('password')
#
#         # Validation
#         value = {
#             'f_name': f_name,
#             'l_name': l_name,
#             'phone': phone,
#             'email': email
#         }
#         error_message = None
#
#         # objects create
#         customer = Customer(f_name=f_name, l_name=l_name, phone=phone, email=email, password=password)
#
#         error_message = self.validate_customer(customer)
#         # Saving data
#         if not error_message:
#             customer.password = make_password(customer.password)
#             # customer.save()
#             customer.regis()  # regis is the method which is define in customer module
#
#             return redirect('products')
#
#         else:
#             data = {
#                 'error': error_message,
#                 'values': value
#             }
#
#             return render(request, 'store/register.html', data)
#
#     def validate_customer(self, customer):
#         error_message = None
#         if (not customer.f_name):
#             error_message = "First name is required!!"
#         elif len(customer.f_name) < 4:
#             error_message = "First name must be 4 char or long!!"
#
#         elif (not customer.l_name):
#             error_message = "Last name is required!!"
#         elif len(customer.l_name) < 4:
#             error_message = "Last name must be 4 char or long!!"
#
#         elif (not customer.phone):
#             error_message = "Phone number is required!!"
#         elif len(customer.phone) < 10:
#             error_message = "Phone number must be 10 digit or long!!"
#
#         elif (not customer.email):
#             error_message = "Email ID is required!!"
#
#         elif (not customer.password):
#             error_message = "Password is required!!"
#         elif len(customer.password) < 8:
#             error_message = "Password must be 8 char or long!!"
#         elif customer.isExists():
#             error_message = 'Your Email ID is already Registered!!'
#         return error_message
#
#     # class Register(View):
#     #     def get(self, request):
#     #         return render(request, 'store/register.html')
#     #
#     #     def post(self, request):
#     #         return regis_user(request)
