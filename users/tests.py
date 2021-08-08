from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        User.objects.create_superuser(
            username='testuser', email='testuser@example.com', password='testuserpass')

    def test_user_login(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testuserpass'
        }
        res = self.client.post(url, data, format='json')
        self.assertIsNotNone(res.json().get('access'))
