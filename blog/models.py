from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    post = models.TextField()
    image = models.ImageField(upload_to='blog/images', blank=True)
    # this will set date to now but we can change it
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

