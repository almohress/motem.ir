from django.db import models
from djrest_wrapper.interfaces import BaseModel


import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('multimedia/', filename)


class Multimedia(BaseModel):
    file = models.FileField(upload_to=get_file_path)
    last_modified = models.DateTimeField(auto_now_add=True)
