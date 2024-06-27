
from django.urls import path, include
import views

urlpatterns = [
    path('register', views.login_view, name='login_view'),
    path('login', views.register_view, name='register_view'),

    path('', views.home_view, name='home'),
    path('profil', views.profil_view, name='profil_view'),
    path('card', views.card_view, name='card_view'),
    path('card', views.card_view, name='notification_view'),
]