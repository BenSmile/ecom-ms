import unittest
from django.test import RequestFactory, TestCase
from django.urls import reverse
from .models import Notification
from .views import notification_list

class TestNotificationListView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user_id = 1  # Utilisateur fictif pour les tests

    def test_notification_list(self):
        # Création de quelques notifications fictives pour l'utilisateur 1
        Notification.objects.create(user_id=self.user_id, message='Notification 1')
        Notification.objects.create(user_id=self.user_id, message='Notification 2')

        # Création de la requête GET à la vue
        url = reverse('notification_list', kwargs={'user_id': self.user_id})
        request = self.factory.get(url)
        response = notification_list(request, user_id=self.user_id)

        # Vérification du code de statut HTTP et du template utilisé
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notification_list.html')

        # Vérification que les notifications sont passées au template correctement
        notifications = response.context_data['notifications']
        self.assertEqual(len(notifications), 2)  # Nous nous attendons à 2 notifications pour cet utilisateur

    def test_notification_list_no_notifications(self):
        # Test lorsque l'utilisateur n'a aucune notification
        url = reverse('notification_list', kwargs={'user_id': self.user_id})
        request = self.factory.get(url)
        response = notification_list(request, user_id=self.user_id)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notification_list.html')

        notifications = response.context_data['notifications']
        self.assertEqual(len(notifications), 0)  # Nous nous attendons à aucune notification pour cet utilisateur

if __name__ == '__main__':
    unittest.main()
