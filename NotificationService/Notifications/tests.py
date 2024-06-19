# Notifications/tests.py

from django.test import TestCase
from .models import Notification

class NotificationTestCase(TestCase):
    def setUp(self):
        Notification.objects.create(order_id=1, message="Test message")

    def test_notification_creation(self):
        notification = Notification.objects.get(order_id=1)
        self.assertEqual(notification.message, "Test message")
