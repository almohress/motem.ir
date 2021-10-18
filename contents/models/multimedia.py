import uuid
import os
import magic
from django.db import models
from djrest_wrapper.interfaces import BaseModel
from djrest_wrapper.exceptions import ValidationErrorExp

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('multimedia/', filename)


class Multimedia(BaseModel):
    file = models.FileField(upload_to=get_file_path)
    last_modified = models.DateTimeField(auto_now_add=True)
    is_video = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'multimedia'
        verbose_name_plural = 'multimedia'


    def save(self, *args, **kwargs):
        mime = magic.Magic(mime=True).from_buffer(
            self.file.file.file.read()).split('/')[0].lower()
        if mime == 'video':
            self.is_video = True
            super().save(args, kwargs)
        elif mime == 'image':
            self.is_video = False
            super().save(args, kwargs)
        else:
            raise ValidationErrorExp('uploaded multimedia should be video or image')
