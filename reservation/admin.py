from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'arrival_time')
    search_fields = ['guest', 'num_of_guests']
    list_filter = ('status', 'guest', 'created_on', 'arrival_time')
