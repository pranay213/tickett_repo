from django.db import models

# Create your models here.
class TicketSignup(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    email=models.EmailField()
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)

class Location(models.Model):
    location=models.CharField(max_length=32)

class Theatre(models.Model):
    theatre=models.CharField(max_length=32)
