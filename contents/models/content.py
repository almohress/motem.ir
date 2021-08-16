from django.db import models
from djrest_wrapper.interfaces import BaseModel
from .category import Category
from .multimedia import Multimedia


class Content(BaseModel):
    title = models.CharField(max_length=50)
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    files = models.ManyToManyField(Multimedia)
