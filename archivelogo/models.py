from django.db import models

# Create your models here.
class Image(models.Model):
    title =models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='pics') 
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title