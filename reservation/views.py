from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.views import View
from .models import Booking
from .forms import BookingForm


class BookingList(generic.ListView):

    model = Booking

    template_name = 'bookings.html'

    def get(self, request, *args, **kwargs):
        booking_list = Booking.objects.all()
        context = {
            'booking_list': booking_list,
            'form': BookingForm(),
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = BookingForm()
        if request.method == 'POST':
            
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                print('error: invalid form')



        context = {'form': form}
        return render(request, self.template_name, context)
