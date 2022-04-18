from django import forms


class DatePickerInput(forms.DateInput):
    """
    class for datetime input field
    """
    input_type = 'datetime'


class TimePickerInput(forms.TimeInput):
    """
    class for time input field
    """
    input_type = 'time'
