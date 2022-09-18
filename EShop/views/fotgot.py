# from django.views import View
# from django.shortcuts import render,redirect
# from django.contrib.auth.hashers import check_password
# from store.models.customer import Customer
# from django.views import View
#
#
# class Forgot(View):
#
#     def get(self, request):
#         return render(request, 'store/forgot.html')
#
#     def post(self, request):
#         if request.method == 'GET':
#             return render(request, 'store/forgot.html')
#         else:
#             email = request.POST.get('email')
#             # password = request.POST.get('password')
#             customer = Customer.get_customer_by_email(email)
#             error_message = None
#             if customer:
#                 val = email==customer
#                 if val:
#                     request.session['customer_id'] = customer.id
#                     request.session['email'] = customer.email
#                     return redirect('login')
#                 else:
#                     error_message = 'Email or Password is invalid!!'
#
#             else:
#                 error_message = 'Email or Password is invalid!!'
#             return render(request, 'store/forgot.html', {'error': error_message})