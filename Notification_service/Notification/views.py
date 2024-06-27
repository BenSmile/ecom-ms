# myapp/views.py

from django.shortcuts import render
from .models import Notification

def notification_list(request, user_id):
    notifications = Notification.objects.filter(user_id=user_id)
    return render(request, 'notification_list.html', {'notifications': notifications})
