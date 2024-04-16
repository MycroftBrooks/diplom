from django.contrib.auth.models import User
from django.db import models
from month.models import MonthField

# Create your models here.

class Treaty(models.Model):
    name = models.CharField('Название договора', null=True, blank=True, max_length=256)
    number = models.BigIntegerField('Номер договора', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата создания договора', auto_now_add=True, auto_created=True)

class Record(models.Model):
    record = models.IntegerField('Показание', null=True, blank=True)
    multiplier = models.FloatField('Тариф', null=True, blank=True)
    treaty = models.ForeignKey(Treaty, on_delete=models.CASCADE)
    month = MonthField(null=True, blank=True)
    updated_at = models.DateTimeField('Дата изменения показания', auto_now=True)
    created_at = models.DateTimeField('Дата первой подачи показания', auto_created=True, auto_now_add=True)
