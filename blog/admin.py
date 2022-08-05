from django.contrib import admin
from .models import Blogpost, Comments
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Blogpost)
class BlogpostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comments)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'content', 'posted_on', 'approved')
    list_filter = ('approved', 'name', 'posted_on')
    search_fields = ['name', 'approved', 'post']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    