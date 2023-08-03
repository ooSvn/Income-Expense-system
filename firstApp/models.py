from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Expense(models.Model):
    amount = models.fields.BigIntegerField()
    date = models.fields.TimeField()
    text = models.fields.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Income(models.Model):
    amount = models.fields.BigIntegerField()
    date = models.fields.TimeField()
    text = models.fields.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
