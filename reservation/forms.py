from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Booking
from .widget import TimePickerInput, DatePickerInput


class BookingForm(ModelForm):
    """
    Booking model form class
    """

    class Meta:
        """
        Meta class for the booking form class,
        defines the fields and how they are handled in the form
        """
        model = Booking
        fields = (
            'num_of_guests',
            'arrival_time',
            'leaving_time',
            'special_requests'
            )
        labels = {
            'num_of_guests': 'Number of Guests',
            'arrival_time': 'Date and time of booking',
            'leaving_time': 'Time of leaving',
            'special_requests': 'Special Requests',
        }

        widgets = {
            'arrival_time': DatePickerInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
                }),
            'leaving_time': TimePickerInput(attrs={'class': 'form-control'}),
        }
