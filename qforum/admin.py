from django.contrib import admin
from .models import Thread, Post, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'topic', 'description', 'category', 'created_on')
    search_fields = ['topic', 'description']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass