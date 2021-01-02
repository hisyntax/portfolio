from django.db import models

# Create your models here.
class Logo(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title


class Backgroundimg(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title

 
class Author(models.Model):
    thumbnail = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.thumbnail

class Message(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='pics')
    author = Author.objects.first()

    def __str__(self):
        return self.title

class Messages(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='pics')
    author = Author.objects.first()

    def __str__(self):
        return self.title

class About(models.Model):
    detail = models.TextField()

    def __str__(self):
        return self.detail

class Mission(models.Model):
    detail = models.TextField()

    def __str__(self):
        return self.detail

class Service(models.Model):
    detail = models.CharField(max_length=200)

    def __str__(self):
        return self.detail

class Team(models.Model):
    thumbnail = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    prof = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class First_advert(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title


class Second_advert(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title