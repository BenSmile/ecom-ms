# Profil/tests.py

from django.test import TestCase, Client
from .models import Customer
import json

class CustomerTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create(
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            phone_number="1234567890"
        )

    def test_create_customer(self):
        response = self.client.post('/api/customer/', json.dumps({
            'firstname': 'Jane',
            'lastname': 'Doe',
            'email': 'jane.doe@example.com',
            'phoneNumber': '0987654321'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_customer(self):
        response = self.client.get(f'/api/customer/{self.customer.id}/')
        self.assertEqual(response.status_code, 200)

    def test_update_customer(self):
        response = self.client.put(f'/api/customer/{self.customer.id}/', json.dumps({
            'firstname': 'Johnny',
            'lastname': 'Doe',
            'email': 'johnny.doe@example.com',
            'phoneNumber': '1111111111'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_customer(self):
        response = self.client.delete(f'/api/customer/{self.customer.id}/')
        self.assertEqual(response.status_code, 200)
