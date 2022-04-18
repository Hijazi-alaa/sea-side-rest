from django.db import models
from cloudinary.models import CloudinaryField


class Announcements(models.Model):
    """
    Model class to define all fields for announcements
    in the database
    """

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1600)
    img = CloudinaryField('image', default='placeholder')

    class Meta:
        """
        Meta class of the announcment model
        """
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"
