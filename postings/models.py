from django.db import models

from core.models import TimeStampModel

class Post(TimeStampModel):
    title     = models.CharField(max_length=100)
    content   = models.CharField(max_length=500)
    image_url = models.CharField(max_length=200)
    user      = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        db_table = "postings" 