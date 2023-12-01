from django.contrib import admin

from .models import Work, Description, Entry
# Register your models here.

admin.site.register(Work)
admin.site.register(Description)
admin.site.register(Entry)