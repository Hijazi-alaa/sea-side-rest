from django.db import models
from cloudinary.models import CloudinaryField


class MenuItems(models.Model):
    """
    Menu model defining all feilds for the model in database
    """
    CATEGORIES = (
        ("Starters", "Starters"),
        ("Main Courses", "Main Courses"),
        ("Side Orders", "Side Orders"),
        ("Desserts", "Desserts"),
    )
    name = models.CharField(max_length=30)
    category = models.CharField(
        max_length=30,
        choices=CATEGORIES,
        default="Main Courses"
        )
    discreption = models.TextField(max_length=800)
    item_img = CloudinaryField('image', blank=True)
    price = models.CharField(max_length=20, default="$10.00")

    class Meta:
        """
        Menu model  meta class
        """
        ordering = ['name']

    def __str__(self):
        return f"{self.name} | {self.category}"
