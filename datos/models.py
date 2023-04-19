from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class TemplateData(models.Model):
	leasid = models.CharField(max_length=10)
	bldgid = models.CharField(max_length=10)
	suitid = models.CharField(max_length=10)
	occpname = models.CharField(max_length=50)
	fields = models.JSONField(null=True)

	def getbuildingsList(self):
		data = TemplateData.objects.all()
		bldgidList = []
		for d in data:
			if d.bldgid:
				bldgidList.append(d.bldgid)
		return bldgidList

	def getLeasIdList(self):
		data = TemplateData.objects.all()
		leasidList = []
		for d in data:
			if d.leasid:
				leasidList.append(d.leasid)
		return leasidList

	def getDataByLeasId(self, leasid):
		data = TemplateData.objects.all().filter(leasid__contains=leasid)
		return data

	def getDataByBuildings(self, building):
		data = TemplateData.objects.all().filter(bldgid__contains=building)
		return data

	def __str__(self):
		template = '{0.leasid} {0.bldgid} {0.suitid} {0.occpname} {0.fields}'
		return template.format(self)

	class Meta:
		verbose_name = 'Dato de Plantilla'
		verbose_name_plural = 'Datos de Plantillas'
		db_table = 'templates_data'
		ordering = ['bldgid']


class TemplateDataLog(models.Model):
	username = models.CharField(default="Null", max_length=30)
	bldgid = models.CharField(max_length=10)
	first_validation = models.BooleanField(default=False)
	second_validation = models.BooleanField(default=False)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		template = '{0.username} {0.bldgid} {0.created}'
		return template.format(self)

	class Meta:
		verbose_name = 'Registro de Dato'
		verbose_name_plural = 'Registros de Datos'
		db_table = 'templates_data_log'
		ordering = ['bldgid']


class TemplateDataUploadLog(models.Model):
	username = models.CharField(max_length=30)
	bldgid = models.CharField(max_length=10)
	active = models.BooleanField(default=True)

	def __str__(self):
		template = '{0.username} {0.bldgid} {0.active}'
		return template.format(self)

	class Meta:
		verbose_name = 'Registro de subida'
		verbose_name_plural = 'Registros de subida'
		db_table = 'templates_data_upload_log'
		ordering = ['bldgid']
