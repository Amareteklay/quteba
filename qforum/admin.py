from django.contrib import admin
from .models import Forum, Discussion
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Forum)
class ForumAdmin(SummernoteModelAdmin):
    list_display = ('topic', 'description', 'status', 'date_created')
    search_fields = ['topic', 'description']
    list_filter = ('status', 'date_created')
    summernote_fields = ('description',)


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    pass