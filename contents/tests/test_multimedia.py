from django.test import TestCase
from django.core.files import File
from ..models import Multimedia
import requests


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
