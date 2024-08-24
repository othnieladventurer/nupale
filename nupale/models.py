from django.db import models
from django.utils import timezone

# Create your models here.


class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    



class Quote(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=timezone.now)


    def __str__(self):
        return f"{self.subject} + {self.first_name} {self.last_name}"



















