from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    """
    Register contact to admin
    """
    list_display = ('name', 'email', 'subject', 'message')
    summernote_fields = ('message',)
