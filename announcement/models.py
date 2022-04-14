from django.db import models
from cloudinary.models import CloudinaryField

class Announcements(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1600)
    img = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
