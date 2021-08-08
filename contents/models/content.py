from django.db import models
from djrest_wrapper.interfaces import BaseModel
from .catagory import Catagory


class Content(BaseModel):
    title = models.CharField(max_length=50)
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
