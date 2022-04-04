from django import forms
from reservation import models

class MakeBooking(forms.Form, models.Book):

    booking_time = forms.DateTimeField(localize=True, required=True)
    Leaving_time = forms.DateTimeField(localize=True, required=True)
    num_of_guests = forms.IntegerField(default=2, required=True)
    special_requests = forms.CharField(max_length=300, initial="Additional info: such as allergies or special requests", required=False)
