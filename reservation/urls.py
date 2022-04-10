from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('edit/<booking_id>', views.edit_booking, name='edit'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
]
