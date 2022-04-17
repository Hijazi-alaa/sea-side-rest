from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm


class BookingList(generic.ListView):

    model = Booking

    template_name = 'bookings.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        booking_list = Booking.objects.filter(guest=user)
        form = BookingForm()
        context = {
            'booking_list': booking_list,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            pre_save_form = form.save(commit=False)
            pre_save_form.guest = User.objects.get(pk=self.request.user.pk)
            pre_save_form.save()
            return redirect('bookings')

        context = {'form': form}
        return render(request, self.template_name, context)


def edit_booking(request, booking_id):
    """
    edit booking in database
    """
    booking = get_object_or_404(Booking, pk=booking_id)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('bookings')
    return render(request, 'update_booking.html', context={
        'form': form,
        'booking': booking,
    })


def delete_booking(request, booking_id):
    """
    delete booking from database
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('bookings')
