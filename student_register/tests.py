from django.test import TestCase
# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
class TestUserRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()
    def test_registration(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status, 200)
        response = self.client.post(url, {})
        self.assertEqual(response.status, 200)
        exp_data = {
            'error': True,
            'errors': {
                'username': 'This field is required',
                'password': 'This field is required',
                'confirm': 'This field is required',
            }
        }
        
        self.asssertEqual(exp_data, response.json())
        req_data = {
            'username': 'vaibhav@gmail.com',
            'password': 'vaibhav',
            'confirm': 'vaibhav1234',
        }
        response = self.client.post(url, req_data)
        self.assertEqual(response.status, 200)
        exp_data = {
            'error': True,
            'errors': {
                'confirm': 'Passwords mismatched'
            }
        }
        self.asssertEqual(exp_data, response.json())

        # test req method POST with valid data
        req_data = {
            'username': 'vaibhav@gmail.com',
            'password': 'vaibhav1234',
            'confirm': 'vaibhav1234',
        }
        response = self.client.post(url, req_data)
        self.assertEqual(response.status, 200)
        exp_data = {
            'error': False,
            'message': 'Success, Please login'
        }
        self.asssertEqual(exp_data, response.json())
        self.assertEqual(User.objects.count(), 1)