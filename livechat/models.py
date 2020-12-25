from django.db import models

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Phone(models.Model):
    title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.title