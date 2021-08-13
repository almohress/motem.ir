from djrest_wrapper.interfaces import BaseService
from django.db import IntegrityError
from djrest_wrapper.exceptions import apis as apiexp


class MultimediaService(BaseService):

    def create_model(self, file, fields: dict):
        try:
            upload_file = self.model.objects.create(file=file)
            model = self.model.objects.get_or_create(**fields)
            return model[0], upload_file
        except IntegrityError:
            raise apiexp.DuplicateModelExp(
                f'This {self.model.__name__} is already exists.')
