from django.db import models
from plantillas.models import Plantilla

# Create your models here.

class ToMri(models.Model):
	BLDGID = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
	LEASID = models.CharField(max_length=10)
	DESCRPTN = models.CharField(max_length=30)
	VALUE = models.DecimalField(max_digits=9, decimal_places=2)

	def __str__(self):
		template = '{0.BLDGID} {0.LEASID} {0.DESCRPTN} {0.VALUE}'
		return template.format(self)