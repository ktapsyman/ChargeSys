from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Goods(models.Model):
	Name = models.CharField(max_length=200)
	Price = models.IntegerField(default=0)

class Receipt(models.Model):
	Goods = models.ForeignKey( Goods, on_delete=models.CASCADE )#models.CharField(max_length=200)
	Amount = models.IntegerField(default=0)
	ShoppingDate = models.DateTimeField()
	RecordDate = models.DateTimeField('date published')

