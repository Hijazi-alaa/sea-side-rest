from django.db import models
from cloudinary.models import CloudinaryField


class Menu_items(models.Model):

    item_name = models.CharField(max_length=30)
    discreption = models.TextField(max_length=400)
    item_img = CloudinaryField('image')

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return self.item_name
