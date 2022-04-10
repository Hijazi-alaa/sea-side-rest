from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm


def home_view(request):
    return render(request, 'home.html')
    

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
        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('/')

        context = {'form': form}
        return render(request, self.template_name, context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'update_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('/')