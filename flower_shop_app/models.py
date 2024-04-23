from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(AbstractUser):
    purchases_counter = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.username

class Flower(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='flowers/', null=False, blank=False)
    price = models.SmallIntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

class Bouquet(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='bouquets/', null=False, blank=False)
    flowers = models.ManyToManyField(Flower)
    price = models.SmallIntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
