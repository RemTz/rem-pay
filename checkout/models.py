from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class PayWay(models.Model):
    PAYMENT_WAYS = (
        ('TG', 'TigoPesa'),
        ('MP', 'M-Pesa'),
        ('TP', 'T-Pesa'),
        ('PP', 'PayPal')
    )
    name = models.CharField(max_length=100, choices = PAYMENT_WAYS)
    amount = models.FloatField(max_length=100, blank= 1)
    time = models.DateTimeField(blank=0)
    customer_name = models.TextField(max_length=225)
    course_name = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.amount}, {self.time}, {self.customer_name}, {self.course_name}' 

class Address(models.Model):
    city = models.TextField(max_length=30, blank=0)

    def __str__(self):
        return self.city

class Price(models.Model):
    original_price = models.FloatField(max_length=20)
    discount_price = models.FloatField(max_length=20)
    total = models.FloatField(blank=1)

    def __str__(self):
        return f'{self.original_price}, {self.discount_price}, {self.total}'

class Orderdetails(models.Model):
    coz_name = models.TextField(max_length=10)
    coz_price = models.TextField(max_length=10)
    issue_date = models.TimeField(blank=0)

    def __str__(self):
        return f'{self.coz_name}, {self.coz_price}, {self.issue_date}'
