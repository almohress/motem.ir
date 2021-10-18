import requests
from rest_framework.test import APITestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.contrib.auth.models import User
from ..models import Category


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
            'username': username,
            'password': password
        }
        response = self.client.post(url, data, format='json')
        return response.json().get('access', None)

    def upload_file(self):
        url = 'https://filesamples.com/samples/image/jpeg/sample_640%C3%97426.jpeg'
        filename = 'multimedia/testjpeg.jpeg'
        with requests.get(url=url, stream=True) as r:
            r.raise_for_status()

            with open(filename, mode='wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        url = reverse('multimedia-list')
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        with open(filename, mode='rb') as handle:
            file = File(handle)
            upload = SimpleUploadedFile(
                filename, file.read(), content_type='multipart/form-data')
            data = {
                'file': upload
            }
            response = self.client.post(url, data, format='multipart')
        return response.json()

    def test_create_category(self):
        files = [self.upload_file() for _ in range(3)]
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('category-list')
        data = {
            'name': 'test',
            'title': 'test title',
            'description': 'test description',
            'files': [file.get('multimedia').get('id') for file in files]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json().get('category'))
        self.assertIsNotNone(response.json().get('category').get('files'))

    def test_list_categories(self):
        for i in range(10):
            Category.objects.create(
                name=f'test {i}', title=f'test {i}', description=f'test {i}')
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('categories'))

    def test_retrieve_category(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        category = Category.objects.create(
            name=f'test', title=f'test', description=f'test')
        url = reverse('category-detail', args={str(category.id)})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('category'))
        self.assertEqual(response.json().get(
            'category').get('id'), str(category.id))

    def test_update_category(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        category = Category.objects.create(
            name=f'test', title=f'test', description=f'test')
        url = reverse('category-detail', args={str(category.id)})
        data = {
            'name': 'new test',
            'title': 'new test',
            'description': 'new test',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('category'))
        for key, value in data.items():
            self.assertEqual(response.json().get('category').get(key), value)

    def test_partial_update_category(self):
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        category = Category.objects.create(
            name=f'test', title=f'test', description=f'test')
        url = reverse('category-detail', args={str(category.id)})
        data = {
            'title': 'new test',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get('category'))
        self.assertEqual(response.json().get(
            'category').get('title'), data.get('title'))
