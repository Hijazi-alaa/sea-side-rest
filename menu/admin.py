from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Menu_items

@admin.register(Menu_items)
class MenuAdmin(SummernoteModelAdmin):

    summernote_fields = ('discreption')
