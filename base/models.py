from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Create Database Table
# python manage.py makemigration
# python manage.py migrate

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # host and topic are aboe the room
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    #null is allowed. when submitting form form being empty is allowed(blank = True)
    description = models.TextField(null=True, blank = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # auto_now will save every update
    # auto_now_add will only save the time when it was first saved/ won't be changed after...
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] # with '-' it will order descending order, without it ascending

    def __str__(self):
        # return str(self.updated) since the method returns string, convert Date to string
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # we want only first 50 characters for preview
        return self.body[0:50]