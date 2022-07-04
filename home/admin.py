from django.contrib import admin
from django.contrib.auth.models import User
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    summernote_fields = ('message',)