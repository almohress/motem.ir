from django.test import TestCase
from django.core.files import File
from ..models import Multimedia


class MultimediaTestCase(TestCase):
    def setUp(self):
        with open('testfile.db', mode='wb') as f:
            f.write(b'\x10')

    def test_create_multimedia(self):
        with File(open('testfile.db', mode='rb')) as f:
            mm = Multimedia.objects.create(file=f)
            self.assertIsNotNone(mm)
