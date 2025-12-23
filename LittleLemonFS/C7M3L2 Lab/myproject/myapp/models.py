from django.db import models
from django.utils import timezone

# Create your models here.

       

class Menu(models.Model):
    title = models.CharField(max_length=255)                     # corresponds to Title
    price = models.DecimalField(max_digits=10, decimal_places=2) # corresponds to Price
    inventory = models.IntegerField()                             # corresponds to Inventory

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


# Booking model
class Booking(models.Model):
    name = models.CharField(max_length=255, default="Anonymous")                       # corresponds to Name
    no_of_guests = models.IntegerField(default=1)                           # corresponds to No_of_guests
    booking_date = models.DateField(default=timezone.now)                         # corresponds to BookingDate

    def __str__(self):
        return f"{self.name} - {self.booking_date}"