from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class CategoryTestCase(APITestCase):
    def setUp(self):
        User.objects.create_superuser(
            username='testuser', email='testuser@example.com', password='testuserpass')

    def login(self, username, password) -> str:
        """
        Returns jwt access token if credentials were valid
        """
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testuserpass'
        }
        response = self.client.post(url, data, format='json')
        return response.json().get('access', None)

    def test_create_category(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('category-list')
        data = {
            'name': 'test',
            'title': 'test title',
            'description': 'test description',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json().get('category'))
