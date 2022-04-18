from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


class BookingList(generic.ListView):
    """
    Booking view handles the view of the booking model
    on the booking template
    """
    model = Booking

    template_name = 'bookings.html'

    def get(self, request, *args, **kwargs):
        """
        get method to define the view of booking lists
        and the booking form
        """
        user = User.objects.get(pk=self.request.user.pk)
        booking_list = Booking.objects.filter(guest=user)
        form = BookingForm()
        context = {
            'booking_list': booking_list,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        post method handles the form validation and adding
        the the form submited to the database
        """
        form = BookingForm(request.POST)
        if form.is_valid():
            submited = form.save(commit=False)
            submited.guest = User.objects.get(pk=self.request.user.pk)
            submited.save()
            messages.success(request, 'Booking Succesfull, \
                 waiting for approval')
            return redirect('bookings')
        else:
            BookingForm()

        context = {'form': form}
        return render(request, self.template_name, context)


def edit_booking(request, booking_id):
    """
    Function to get an already made booking
    and update its information using a form
    """
    booking = get_object_or_404(Booking, pk=booking_id)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        messages.success(request, 'Booking Succesfull Updated')
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
    messages.success(request, 'Booking deleted!')
    return redirect('bookings')
