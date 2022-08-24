from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blogpost, Comments


@admin.register(Blogpost)
class BlogpostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'process', 'created_on')
    list_display = ('title', 'slug', 'category', 'created_on', 'process')
    search_fields = ['title', 'content', 'category']
    summernote_fields = ('content')


@admin.register(Comments)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'content', 'posted_on', 'approved')
    list_filter = ('approved', 'name', 'posted_on')
    search_fields = ['name', 'approved', 'post']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
