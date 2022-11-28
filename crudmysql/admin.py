from django.contrib import admin
from .models import student1


@admin.register(student1)
class student1Admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','city')

    