from django.views.generic.list import ListView
from .models import Announcements


class MyAnnouncement(ListView):
    """
    View class defines the view of the Announcments model
    """
    model = Announcements
    template_name = 'home.html'
