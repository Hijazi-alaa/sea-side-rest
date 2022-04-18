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

    def accepted_times(self):
        """
        function defining accepting criteria
        for the arrival and leaving time fields.
        """
        arrival_time = self.cleaned_data.get('arrival_time')
        leaving_time = self.cleaned_data.get('leaving_time')

        if not arrival_time < leaving_time:
            raise ValidationError(
                "Something is not right, Your leaving time \
                    should not be before your arrival."
            )
        else:
            return self.changed_data
