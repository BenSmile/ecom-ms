import json
import unittest
from unittest.mock import patch
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.http import JsonResponse
from .models import Customer
from .views import create_customer, get_customers, get_customer, update_customer, delete_customer

class TestCustomerViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @patch('.views.Customer.objects.create')
    def test_create_customer(self, mock_create):
        # Données de requête simulées
        data = {
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'phoneNumber': '1234567890'
        }
        request = self.factory.post('/customer', data=json.dumps(data), content_type='application/json')
        mock_create.return_value = Customer(id=1)  # Simuler la création d'un client avec ID 1

        response = create_customer(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'id': 1})

    @patch('.views.Customer.objects.all')
    def test_get_customers(self, mock_all):
        # Simuler la liste de tous les clients
        mock_all.return_value = Customer.objects.all()

        request = self.factory.get('/get_customers')
        response = get_customers(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn('customers', response.json())

    @patch('.views.get_object_or_404')
    def test_get_customer(self, mock_get_object_or_404):
        # Simuler la récupération d'un client spécifique
        customer = Customer(id=1, firstname='John', lastname='Doe', email='john.doe@example.com', phoneNumber='1234567890')
        mock_get_object_or_404.return_value = customer

        request = self.factory.get(reverse('get_customer', kwargs={'id': 1}))
        response = get_customer(request, id=1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)
        self.assertEqual(response.json()['firstname'], 'John')

    @patch('.views.get_object_or_404')
    @patch('.views.Customer.save')
    def test_update_customer(self, mock_save, mock_get_object_or_404):
        # Simuler la mise à jour d'un client existant
        customer = Customer(id=1, firstname='John', lastname='Doe', email='john.doe@example.com', phoneNumber='1234567890')
        mock_get_object_or_404.return_value = customer

        data = {
            'firstname': 'Jane',
            'lastname': 'Doe',
            'email': 'jane.doe@example.com',
            'phoneNumber': '9876543210'
        }
        request = self.factory.put(reverse('update_customer', kwargs={'id': 1}), data=json.dumps(data), content_type='application/json')

        response = update_customer(request, id=1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Customer updated'})

    @patch('.views.get_object_or_404')
    @patch('.views.Customer.delete')
    def test_delete_customer(self, mock_delete, mock_get_object_or_404):
        # Simuler la suppression d'un client existant
        customer = Customer(id=1, firstname='John', lastname='Doe', email='john.doe@example.com', phoneNumber='1234567890')
        mock_get_object_or_404.return_value = customer

        request = self.factory.delete(reverse('delete_customer', kwargs={'id': 1}))
        response = delete_customer(request, id=1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Customer deleted'})

if __name__ == '__main__':
    unittest.main()
