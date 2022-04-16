from datetime import datetime
from django.forms import ModelForm
from .models import Booking
from .widget import TimePickerInput, DateTimePickerInput


class BookingForm(ModelForm):
    current_datetime = datetime.now()
    arrival_time = current_datetime.strftime('%Y-%m-%d %H:%M')

    class Meta:
        model = Booking
        fields = ['num_of_guests', 'arrival_time', 'leaving_time', 'special_requests',]

        widgets = {
            'leaving_time': TimePickerInput(),
            'arrival_time': DateTimePickerInput(),
        }
