# myapp/models.py

from django.db import models

class Notification(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for user {self.user_id} at {self.created_at}"
