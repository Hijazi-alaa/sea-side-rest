from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'arrival_time')
    search_fields = ['guest', 'num_of_guests']
    list_filter = ('status', 'guest', 'created_on', 'arrival_time')
