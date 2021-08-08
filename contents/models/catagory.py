from django.db import models
from djrest_wrapper.interfaces import BaseModel
from .multimedia import Multimedia


class Catagory(BaseModel):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    files = models.ManyToManyField(Multimedia)
