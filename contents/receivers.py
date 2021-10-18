from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Multimedia


@receiver(post_delete, sender=Multimedia)
def remove_file_from_s3(sender, instance, **kwargs):
    instance.file.delete(save=False)
