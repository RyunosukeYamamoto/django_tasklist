from django.db import models

class User(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name