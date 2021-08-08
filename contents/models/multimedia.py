import uuid
import os
import magic
from django.db import models
from djrest_wrapper.interfaces import BaseModel


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('multimedia/', filename)


class Multimedia(BaseModel):
    file = models.FileField(upload_to=get_file_path)
    last_modified = models.DateTimeField(auto_now_add=True)
    is_video = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if magic.Magic(mime=True).from_buffer(self.file.file.file.read()).split('/')[0].lower() == 'video':
            self.is_video = True
        super().save(args, kwargs)
