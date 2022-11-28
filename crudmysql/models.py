from django.db import models

# Create your models here.
class student1(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)