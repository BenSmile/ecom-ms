import unittest
from unittest.mock import patch, MagicMock
from django.test import RequestFactory
from . import views 

class TestViews(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_login_view(self):
        request = self.factory.get('login_view')
        response = views.login_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_view(self):
        request = self.factory.get('register_view')
        response = views.register_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    @patch('requests.get')
    @patch('requests.Session')
    def test_home_view(self, mock_session, mock_get):
        request = self.factory.get('home')
        request.COOKIES = {'access_token': 'valid_access_token'}

        mock_session.return_value = MagicMock()
        mock_session.return_value.get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'product_id': 1, 'name': 'Product 1'}]

        response = views.home_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    @patch('requests.get')
    def test_card_view(self, mock_get):
        request = self.factory.get('cards_view')
        request.COOKIES = {'access_token': 'valid_access_token'}

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'card_id': 1, 'name': 'Card 1'}]

        response = views.card_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cards.html')

    @patch('requests.get')
    def test_profil_view(self, mock_get):
        request = self.factory.get('profil_view')
        request.COOKIES = {'access_token': 'valid_access_token'}

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'user_id': 1, 'username': 'test_user'}

        response = views.profil_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profil.html')

    @patch('requests.get')
    def test_notification_view(self, mock_get):
        request = self.factory.get('notifications_view')
        request.COOKIES = {'access_token': 'valid_access_token'}

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'notification_id': 1, 'message': 'Notification 1'}]

        response = views.notification_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notifications.html')

if __name__ == '__main__':
    unittest.main()
