from django.db import models
from django.core.validators import MaxValueValidator
# import datetime
# Create your models here.

class booking (models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    bookingdate = models.DateTimeField()


class menu (models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(5)])


