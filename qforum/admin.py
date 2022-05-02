from django.contrib import admin
from .models import Thread, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):
    list_display = ('name', 'topic', 'slug', 'description', 'category', 'created_on')
    search_fields = ['topic', 'description']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('topic',)}
    summernote_fields = ('description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'thread', 'parent', 'content', 'created', 'active')
    search_fields = ['name', 'email', 'content']
    list_filter = ('active', 'created', 'updated')
    summernote_fields = ('body',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass