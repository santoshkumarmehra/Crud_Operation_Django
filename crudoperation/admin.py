from django.contrib import admin
from .models import PeopleData


@admin.register(PeopleData)
class PeopleDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','city')
