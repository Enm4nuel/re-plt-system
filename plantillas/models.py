from django.db import models
from django.utils import timezone
from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Template(models.Model):
	bldgid = models.CharField(max_length=10)
	currcode = models.CharField(max_length=10)
	fields = models.JSONField(null=True)
	#inccat = models.CharField(max_length=10)
	#descrptn = models.CharField(max_length=30)

	def getIncome(self, bldgid, currcode):
		if self.bldgid == bldgid and self.currcode == currcode:
			return "{}".format(self.fields)

	def bldgsToList(self):
		return "{}".format(self.bldgid)

	def __str__(self):
		return self.bldgid

	class Meta:
		verbose_name = 'Plantilla'
		verbose_name_plural = 'Plantillas'
		db_table = 'templates'
		ordering = ['bldgid', 'currcode']

class TemplateLog(models.Model):
	username = models.CharField(max_length=30, default="Null")
	bldgid = models.CharField(max_length=10)
	batch = models.CharField(max_length=8, default="Null")
	rate = models.DecimalField(max_digits=9, decimal_places=6, default=1)
	invoice_date = models.DateField(default=date.today)
	created = models.DateTimeField(default=timezone.now)

	def getLastBatch(self):
		data = TemplateLog.objects.order_by('-batch')
		return data[0]

	def __str__(self):
		return "{}, {}".format(self.batch, self.invoice_date)

	class Meta:
		verbose_name = 'Registro de Plantillas'
		verbose_name_plural = 'Registros de Plantillas'
		db_table = 'templates_log'
		ordering = ['bldgid', 'batch']