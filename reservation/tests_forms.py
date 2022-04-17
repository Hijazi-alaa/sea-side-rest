from django.test import TestCase
from .forms import BookingForm

class TestBookingForm(TestCase):

    def test_item_arrival_time_is_required(self):
        form = BookingForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('arrival_time', form.errors.keys())
        self.assertEqual(form.errors['arrival_time'][0], 'This field is required.')

    def test_special_requests_is_not_required(self):
        form = BookingForm({'name': 'Test Booking Form'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['num_of_guests', 'arrival_time', 'leaving_time', 'special_requests',])
