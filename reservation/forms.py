from django.forms import ModelForm
from .models import Booking
from .widget import TimePickerInput, DateTimePickerInput

class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ('guest', 'num_of_guests', 'arrival_time', 'leaving_time', 'special_requests',)

        widgets = {
            'leaving_time': TimePickerInput(),
            'arrival_time': DateTimePickerInput(),
        }

