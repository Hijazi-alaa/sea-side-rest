from django.shortcuts import render
from django.views import generic
from .models import Book


class BookingList(generic.ListView):
    
    model = Book

    template_name = 'bookings.html'
