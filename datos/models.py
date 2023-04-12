from django.db import models

# Create your models here.

class Datosp(models.Model):
	leasid = models.CharField(max_length=10)
	bldgid = models.CharField(max_length=10)
	suitid = models.CharField(max_length=10)
	occpname = models.CharField(max_length=50)
	values = models.JSONField(null=True)

	def __str__(self):
		template = '{0.leasid} {0.bldgid} {0.suitid} {0.occpname} {0.values}'
		return template.format(self)

# esta clase se usa en el template "postear datos".
class LogDatosP(models.Model):
	username = models.CharField(max_length=30)
	building = models.CharField(max_length=10)
	real = models.BooleanField(default=False)
	real2 = models.BooleanField(default=False)
	created = models.DateTimeField()

	def __str__(self):
		template = '{0.username} {0.building} {0.created}'
		return template.format(self)


class LogSubirDatosP(models.Model):
	username = models.CharField(max_length=30)
	building = models.CharField(max_length=10)
	active = models.BooleanField(default=True)

	def __str__(self):
		template = '{0.username} {0.building} {0.active}'
"""
class DatosTcam(models.Model):
	leasid = models.CharField(max_length=10)
	bldgid = models.CharField(max_length=10)
	suitid = models.CharField(max_length=10)
	occpname = models.CharField(max_length=50)
	values = models.JSONField(null=True)

	def __str__(self):
		template = '{0.leasid} {0.bldgid} {0.suitid} {0.occpname} {0.values}'
		return template.format(self)

class DatosBmSdc(models.Model):
	leasid = models.CharField(max_length=10)
	bldgid = models.CharField(max_length=10)
	suitid = models.CharField(max_length=10)
	occpname = models.CharField(max_length=50)
	values = models.JSONField(null=True)

	def __str__(self):
		template = '{0.leasid} {0.bldgid} {0.suitid} {0.occpname} {0.values}'
		return template.format(self)

class DatosBmPcc(models.Model):
	leasid = models.CharField(max_length=10)
	bldgid = models.CharField(max_length=10)
	suitid = models.CharField(max_length=10)
	occpname = models.CharField(max_length=50)
	values = models.JSONField(null=True)

	def __str__(self):
		template = '{0.leasid} {0.bldgid} {0.suitid} {0.occpname} {0.values}'
		return template.format(self)
"""