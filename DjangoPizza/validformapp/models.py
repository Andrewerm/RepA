from django.db import models

# Create your models here.

class Phonebook(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    description=models.TextField()
