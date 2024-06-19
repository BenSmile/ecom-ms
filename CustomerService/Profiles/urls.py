# customer/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('profil/', create_Profil, name='create_profil'),
    path('profil/<int:profil_id>/', get_Profil, name='get_profil'),
    path('profil/<int:profil_id>/', update_Profil, name='update_profil'),
    path('profil/<int:profil_id>/', delete_Profil, name='delete_profil'),
]
