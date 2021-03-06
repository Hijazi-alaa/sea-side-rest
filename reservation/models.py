from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Pending"), (1, "Booked"))


class Booking(models.Model):
    """
    Booking model defines all the fields
    of the Booking model in the database
    """
    created_on = models.DateTimeField(auto_now=True)
    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booker",
        null=True
        )
    updated_on = models.DateTimeField(auto_now=True)
    num_of_guests = models.PositiveIntegerField(default=2)
    arrival_time = models.DateTimeField()
    leaving_time = models.TimeField(blank=True)
    special_requests = models.TextField(max_length=300, blank=True,)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Meta class for Booking model
        """
        ordering = ["-created_on"]

    def __str__(self):
        return f"booking time: {self.arrival_time} number of guests:\
            {self.num_of_guests}"
