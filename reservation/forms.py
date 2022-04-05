from django import forms
from django.contrib.auth.models import User
from .models import Book

class BookingForm(forms.ModelForm):
    name = forms.CharField(required=True)
    size_of_party = forms.ChoiceField(initial=2, label="Size of party")
    booking_time = forms.DateTimeField(localize=True, label="Time of Arrival")
    until = forms.DateTimeField(localize=True, label="Until")
    requests = forms.TextInput()

    class Meta:
        model = Book
        fields = ('guest', 'num_of_guests', 'arrival_time', 'leaving_time', 'special_requests',)