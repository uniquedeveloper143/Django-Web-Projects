from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Eshop import settings
# from .views import home, login, register
from .views import Index,Register,Login,logout,Cart,CheckOut,OrderPlace,profile,address,change_password,update_profile,UpdatePass,add_address,view_add,delete_add,edit_data_add,edit_add
# from .views import login
from .middlewares.auth import auth_middleware


urlpatterns = [
                  path('', Index.as_view(), name="products"),
                  # path('register', Register,name="register"), # this is function based views
                  path('register', Register.as_view(), name="register"),
                  # path('login', login, name="login"), # this is function based views
                  path('login', Login.as_view(), name="login"),
                  path('update_pass', UpdatePass.as_view(), name="update_pass"),
                  path('logout', logout, name="logout"),
                  path('profile', profile, name="profile"),
                  path('update_profile', update_profile, name="update_profile"),
                  path('address', address, name="address"),
                  path('add_address', add_address, name="add_address"),
                  path('view_address', view_add, name="view_address"),
                  path('delete(<int:eid>)', delete_add, name='delete'),
                  path('edit_add(<int:eid>)', edit_add, name='edit_add'),
                  path('edit_data_add/<int:eid>', edit_data_add, name='edit_data_add'),
                  path('change_password', change_password, name="change_password"),
                  path('cart', Cart.as_view(), name="cart"),
                  path('check-out', auth_middleware(CheckOut.as_view()), name="checkout"),
                  # path('check-out', CheckOut.as_view(), name="checkout"),
                  path('orders', auth_middleware(OrderPlace.as_view()), name="orders"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
