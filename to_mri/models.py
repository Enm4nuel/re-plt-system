from django.db import models
from plantillas.models import Plantilla

# Create your models here.

class ToMri(models.Model):
	bldgid = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
	leasid = models.CharField(max_length=10)
	descrptn = models.CharField(max_length=30)
	value = models.DecimalField(max_digits=9, decimal_places=2)

	def __str__(self):
		template = '{0.bldgid} {0.leasid} {0.descrptn} {0.value}'
		return template.format(self)