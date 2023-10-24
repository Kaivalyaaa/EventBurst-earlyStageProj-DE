# events/models.py
from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

class User(models.Model):#--------for user-admin
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # Use a secure way to store passwords, like hashing

    def __str__(self):
        return self.username

class AdminUser(models.Model):#--------for user-admin
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
