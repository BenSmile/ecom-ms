# myapp/urls.py

from django.urls import path
from .views import notification_list

urlpatterns = [
    path('notifications/<int:user_id>', notification_list, name='notification_list'),
]
