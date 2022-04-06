from django import forms


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'
