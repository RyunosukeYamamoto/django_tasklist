from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)
