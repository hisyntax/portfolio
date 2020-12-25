from django.db import models

# Create your models here.
class  Info(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class Facebook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Instagram(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title