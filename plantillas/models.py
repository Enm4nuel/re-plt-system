from django.db import models

# Create your models here.

class Plantilla(models.Model):
	bldgid = models.CharField(max_length=10)
	currcode = models.CharField(max_length=10)
	inccat = models.CharField(max_length=10)
	descrptn = models.CharField(max_length=30)

	def __str__(self):
		return self.bldgid