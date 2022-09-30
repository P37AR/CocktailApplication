from django.db import models

from embed_video.fields import EmbedVideoField


# Create your models here.
class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.URLField()
    video = models.URLField()
    recipe = models.CharField(max_length=1000)


class Video(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    class Meta:
        ordering = ['-added']
