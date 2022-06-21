from unicodedata import name
from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.TextField(max_length=30)
    age=models.IntegerField