from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Receipt( models.Model ):
	ItemName=models.CharField( max_length=60 )
	TotalCost=models.PositiveIntegerField()
	ShoppingDate=models.DateField()
	def __str__(self):
		return self.ItemName

