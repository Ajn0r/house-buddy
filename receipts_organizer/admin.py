from django.contrib import admin
from .models import Categories, Entries
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Entries)
class EntriesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'amount')