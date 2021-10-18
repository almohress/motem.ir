import requests
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from ..models import Multimedia


class MultimediaTestCase(TestCase):
    def setUp(self):
        url = 'https://filesamples.com/samples/image/jpeg/sample_640%C3%97426.jpeg'
        filename = 'testjpeg.jpeg'
        with requests.get(url=url, stream=True) as r:
            r.raise_for_status()

            with open(filename, mode='wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    def test_create_multimedia(self):
        with File(open('testjpeg.jpeg', mode='rb')) as f:
            mm = Multimedia.objects.create(file=f)
            self.assertIsNotNone(mm)


class MultimediaAPITestCase(APITestCase):
    def setUp(self):
        url = 'https://filesamples.com/samples/image/jpeg/sample_640%C3%97426.jpeg'
        filename = 'multimedia/testjpeg.jpeg'
        with requests.get(url=url, stream=True) as r:
            r.raise_for_status()

            with open(filename, mode='wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        User.objects.create_superuser(
            username='testuser',
            email='testuser@example.com',
            password='testuserpass')

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

    def test_create_multimedia(self):
        url = reverse('multimedia-list')
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        with open('multimedia/testjpeg.jpeg', mode='rb') as handle:
            file = File(handle)
            upload = SimpleUploadedFile(
                'multimedia/testjpeg.jpeg', file.read(),
                content_type='multipart/form-data')
            data = {
                'file': upload
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(response.json().get('multimedia'))

    def test_delete_multimedia(self):
        url = reverse('multimedia-list')
        token = self.login('testuser', 'testuserpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        with open('multimedia/testjpeg.jpeg', mode='rb') as handle:
            file = File(handle)
            upload = SimpleUploadedFile(
                'multimedia/testjpeg.jpeg', file.read(),
                content_type='multipart/form-data')
            data = {
                'file': upload
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(response.json().get('multimedia'))
        m_id = response.json().get('multimedia').get('id')
        url = reverse('multimedia-detail', args={m_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
