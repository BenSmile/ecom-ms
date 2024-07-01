from django.urls import path
from .views import *

urlpatterns = [
    path('', list_users, name='users_list'),  # Lister tous les users
    path('login', login_view, name='login'), # Login
    path('logout', logout_view, name='logout'), # Logout
    path('register', register_view, name='register'), # Enregistrement du user
    path('get-user/<int:user_id>', read_user, name='get_user'),  # Récupérer un user par son ID
    path('update/<int:pk>', update_user, name='update'),  # Mettre à jour un user
    path('delete/<int:pk>', delete_user, name='delete'),  # Supprimer un user
]
