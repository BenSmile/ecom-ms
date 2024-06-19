# Notifications/urls.py

from django.urls import path
from .views import start_consumer

urlpatterns = [
    path('start-consumer/', start_consumer, name='start_consumer'),
]
