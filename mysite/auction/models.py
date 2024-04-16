from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class Car(models.Model):
    category = models.CharField(max_length=100)
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    year = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    with_photo = models.ImageField(upload_to="images/", blank=True, null=True)
    color = models.CharField(max_length=100)
    volume = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Bet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    number = models.IntegerField()
    total_number = models.IntegerField()
    buy_now = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.car} - {self.number}'
