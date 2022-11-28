from django.db import models


class student2(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
