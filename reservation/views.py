from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.views import View
from .models import Book
from .forms import BookingForm


class BookingList(generic.ListView):

    model = Book

    template_name = 'bookings.html'

    def get(self, request, *args, **kwargs):
        book_list = Book.objects.all()
        context = {
            'book_list': book_list,
            'form': BookingForm(),
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            self.template_name, {'form': booking_form}
            )
