from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MenuItems


@admin.register(MenuItems)
class MenuAdmin(SummernoteModelAdmin):
    """
    Class for menu admina panel view
    defining summernote fields
    """
    summernote_fields = ('discreption')
    search_fields = ['name']
    list_filter = ('category',)
