# Notifications/models.py

from django.db import models

class Notification(models.Model):
    order_id = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for Order ID: {self.order_id}"
