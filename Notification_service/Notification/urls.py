# myapp/urls.py

from django.urls import path
from .views import notification_list
import notification_consumer

urlpatterns = [
    path('/<int:user_id>', notification_list, name='notification_list'),
    path('/create/<int:user_id>', notification_consumer.callback, name='create_notification'),
]
