from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Pending"), (1, "Booked"))

class Book(models.Model):

    created_on = models.DateTimeField(auto_now=True)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    num_of_guests = models.PositiveIntegerField(default=2)
    arrival_time = models.DateTimeField()
    leaving_time = models.TimeField()
    special_requests = models.TextField(max_length=300, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return f"booking {self.id}, time: {self.arrival_time} number of seats: {self.num_of_guests}"
