from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Announcements

class MyAnnouncement(ListView):

    model = Announcements
    # queryset = Announcements.objects.all()
    template_name = 'home.html'
