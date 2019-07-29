# Please ignore, was added from as a side lesson from Josh

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    shoe_size = models.IntegerField()


