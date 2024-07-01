# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.create_customer, name='create_customer'),
    path('customers', views.get_customers, name='get_customers'),
    path('customer-login', views.login_customer, name='login_customer'),
    path('customer-get', views.get_customer, name='get_customer'),
    path('customers/<int:id>', views.update_customer, name='update_customer'),
    path('customers/<int:id>', views.delete_customer, name='delete_customer'),
]
