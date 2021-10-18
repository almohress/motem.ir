from django.db import models
from djrest_wrapper.interfaces import BaseModel


class Content(BaseModel):
    title = models.CharField(max_length=50)
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(
        'contents.Category', related_name='category', on_delete=models.CASCADE)
    files = models.ManyToManyField('contents.Multimedia')

    class Meta:
        verbose_name = 'content'
        verbose_name_plural = 'contents'
