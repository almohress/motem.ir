from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Content, Category


class ContentTestCase(APITestCase):
    def setUp(self):
        User.objects.create_superuser(
            username='testuser', email='testuser@example.com', password='testuserpass')
        self.category = Category.objects.create(
            name=f'test', title=f'test', description=f'test')

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

    def test_create_content(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('content-list')
        data = {
            'title': 'test',
            'body': 'test title',
            'is_published': False,
            'category': str(self.category.id),
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json().get('content'))

    def test_list_all_contents(self):
        for i in range(10):
            Content.objects.create(
                body=f'test {i}', title=f'test {i}', is_published=bool(i % 2), category=self.category)
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('content-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('contents'))

    def test_list_published_contents(self):
        for i in range(10):
            Content.objects.create(
                body=f'test {i}', title=f'test {i}', is_published=bool(i % 2), category=self.category)
        url = reverse('content-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('contents'))
        for content in response.json().get('contents'):
            self.assertEqual(content.get('is_published'), True)

    def test_retrieve_content(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        content = Content.objects.create(
            title=f'test', body=f'test', category=self.category)
        url = reverse('content-detail', args={str(content.id)})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('content'))
        self.assertEqual(response.json().get(
            'content').get('id'), str(content.id))

    def test_update_content(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        content = Content.objects.create(
            title=f'test', body=f'test', category=self.category)
        url = reverse('content-detail', args={str(content.id)})
        data = {
            'body': 'new test',
            'title': 'new test',
            'is_published': True,
            'category': str(self.category.id),
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('content'))
        for key, value in data.items():
            self.assertEqual(response.json().get('content').get(key), value)

    def test_partial_update_content(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        content = Content.objects.create(
            title=f'test', body=f'test', category=self.category)
        url = reverse('content-detail', args={str(content.id)})
        data = {
            'title': 'new test',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('content'))
        self.assertEqual(response.json().get(
            'content').get('title'), data.get('title'))
