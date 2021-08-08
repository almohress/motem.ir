from django.db import models
from djrest_wrapper.interfaces import BaseModel


class Catagory(BaseModel):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
