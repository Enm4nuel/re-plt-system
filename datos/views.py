from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import date

from .models import TemplateData, TemplateDataLog, TemplateDataUploadLog
from plantillas.models import *


def visualizar_data(request, filename, workbook):

	sheet = workbook.active

	building = ""

	columnas = []
	for col in sheet.iter_cols():
		columnas.append(col[0].value)

	for row in sheet.iter_rows(min_row=2):
		Datosp.objects.filter(bldgid=row[2].value).delete()
		print("listo")
		break

	for row in sheet.iter_rows(min_row=2):
		data = {}
		for c in range(5,len(columnas)):
			data[str(columnas[c])] = row[c].value
		agregar_Datosp(row[1].value, row[2].value, row[3].value, row[4].value, data)
		building = row[2].value
		print("Se han agregado los datos nuevos a ", row[2].value)

	agregar_LogDatosp(request.user.username, building)

	return 0


def deleteData(bldgid):
	# Eliminar data previamente subida a la db
	try:
		TemplateData.objects.filter(bldgid__contains=bldgid).delete()
	except:
		print("paso algo malo")


def getRate():

	ap = TemplateMonthlyCfg.objects.order_by('-date')[:1]
	print(ap)
	return ap[0].rate


def uploadDataToDb(request, workbook):
	
	# Accedo a los datos de la hoja activa o en uso del archivo excel
	sheet = workbook.active

	# Verificar si existe la data y eliminar en caso de que si
	for row in sheet.iter_rows(min_row=2):
		if TemplateData.objects.filter(bldgid__contains=row[2].value).exists():
			TemplateData.objects.filter(bldgid=row[2].value).delete()
			print("listo")
		break

	# Extraer las columnas que conforman el archivo de plantilla que se esta subiendo
	columns = []
	for col in sheet.iter_cols():
		columns.append(col[0].value)

	# estableciendo una variable con valor "4", ya que las plantillas se conforman de 4 columnas
	# predeterminadas con cada plantilla - Esto puede mejorar -
	limit = 4

	# Obtener el nombre del edificio que se esta cargando
	filtr = ""

	# Obtener taza definida para la facturacion de dicho mes
	rate = getRate()

	# Agregando los datos extraidos a la tabla
	for row in sheet.iter_rows(min_row=2):
		data = {}
		for c in range(limit+1,len(columns)):
			data[str(columns[c])] = float(row[c].value)
		# Evaluar si la informacion que se esta suministrando es correcta
		if Template.objects.filter(bldgid__contains=row[2].value).exists():
			templateData(1, row[1].value, row[2].value, row[3].value, row[4].value, data)
			print("Se han agregado los datos nuevos a ", row[2].value)
			filtr = row[2].value
		else:
			print("La informacion suministrada no es correcta")
			return False
	
	if filtr !="":
		templateDataUploadLog(1, request.user.username, filtr)

	return True


def templateData(option, d1, d2, d3, d4, d5):
	
	# Para agregar datos a la tabla "template_data"
	if option == 1:
		d = TemplateData(leasid=d1, bldgid=d2, suitid=d3, occpname=d4, fields=d5)
		d.save()


def templateDataLog(option, d1, d2, d3, d4):
	
	# Agrega los datos cargados directamente desde la plantilla .xlsx
	# Primero confirma si existe y edita, caso contrario crea
	# De paso asigna True a el campo "First_validation" por default
	if option == 1:

		if TemplateDataLog.objects.filter(bldgid=d2).exists():
			d = TemplateDataLog.objects.get(bldgid=d2)
			d.username = d1
			d.bldgid = d2
			d.first_validation = d3
			d.save()
		else:
			d = TemplateDataLog(
				username=d1, 
				bldgid=d2, 
				first_validation=d3
			)
			d.save()

	# Asignar como True el campo "second_validation"
	elif option == 2:
		d = TemplateDataLog.objects.get(id=d1)
		d.second_validation = d2
		d.save()


def templateDataUploadLog(option, d1, d2):

	if option == 1:
		d = TemplateDataUploadLog(username=d1, bldgid=d2)
		d.save()

	elif option == 2:
		TemplateDataUploadLog.objects.filter(username=d1).delete()

