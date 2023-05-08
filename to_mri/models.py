from django.db import models
from plantillas.models import *

# Create your models here.

class ToMri(models.Model):
	cmbatch = models.CharField(max_length=10) # numero de batch
	item = models.IntegerField() # por cada fila incrementa su valor, de 1 a n numeros
	bldgid = models.CharField(max_length=10) # edificio al que se esta facturando
	leasid = models.CharField(max_length=10) # numero de contrato
	trandate = models.DateField() # fecha de facturacion
	inccat = models.CharField(max_length=6) # income category
	srccode = models.CharField(max_length=2, default="CH") # por default es CH, source code y ch es que se va facturar
	descrptn = models.CharField(max_length=50) # descripcion breve de este campo
	tranamt = models.DecimalField(max_digits=9, decimal_places=2) # valor a facturar
	taxitem = models.CharField(default="N", max_length=1) # por default lleva N
	rtaxgrpid = models.CharField(max_length=6) # se extrae de una vista X
	department = models.CharField(default="@", max_length=30) # por default lleva @
	currcode = models.CharField(max_length=3) # Moneda en la que se esta facturando
	bcurcode = models.CharField(max_length=3, default="DOP") # moneda base 

	def __str__(self):
		template = '{0.bldgid} {0.leasid} {0.descrptn} {0.tranamt}'
		return template.format(self)

	class Meta:
		verbose_name = 'Dato para MRI'
		verbose_name_plural = 'Datos para MRI'
		db_table = 'tomri_data'
		ordering = ['item']