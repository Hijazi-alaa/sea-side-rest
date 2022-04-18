from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Class to configure the view of the admin
    panel for the booking model adds summernote fields.
    """
    list_filter = ('status', 'arrival_time')
    search_fields = ['guest', 'num_of_guests']
    list_filter = ('status', 'guest', 'created_on', 'arrival_time')
