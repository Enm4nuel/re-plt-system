from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import TemplateData, TemplateDataLog, TemplateDataUploadLog


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

def visualizar_data2(filename, workbook):

	sheet = workbook.active

	columnas = []
	for col in sheet.iter_cols():
		columnas.append(col[0].value)

	if 't-cam' in filename:
		DatosTcam.objects.all().delete()
	elif 'bm-sdc' in filename:
		DatosBmSdc.objects.all().delete()
	elif 'bm-pcc' in filename:
		DatosBmPcc.objects.all().delete()

	for row in sheet.iter_rows(min_row=2):
		data = {}
		for c in range(5,len(columnas)):
			data[str(columnas[c])] = row[c].value

		if 't-cam' in filename:
			agregar_DatosTcam(row[1].value, row[2].value, row[3].value, row[4].value, data)
			print("Se han agregado los datos nuevos a T-CAM")
		elif 'bm-sdc' in filename:
			agregar_DatosBmSdc(row[1].value, row[2].value, row[3].value, row[4].value, data)
			print("Se han agregado los datos nuevos a BM-SDC")
		elif 'bm-pcc' in filename:
			agregar_DatosBmPcc(row[1].value, row[2].value, row[3].value, row[4].value, data)
			print("Se han agregado los datos nuevos a BM-PCC")
		else:
			print("No se pudo agregar los datos a la base de datos...")

	return 0
	#return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columnas': columnas, 'rows': rows})

def uploadDataToDb():
	pass

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

		if TemplateDataLog.objects.filter(bldgid_id=d2).exists():
			d = TemplateDataLog.objects.get(bldgid_id=d2)
			d.username = d1
			d.bldgid = d2
			d.first_validation = d3
			d.second_validation = d4
			d.created = timezone.now()
			d.save()
		else:
			d = TemplateDataLog(
				username=d1, 
				bldgid_id=d2, 
				first_validation=d3, 
				second_validation=d4, 
				created=timezone.now()
				)
			d.save()

	# Asignar como True el campo "second_validation"
	elif option == 2:
		d = LogDatosP.objects.get(id=d1)
		d.real2 = d2
		d.created = timezone.now()
		d.save()


def templateDataUploadLog(option, d1, d2):

	if option == 1:
		d = TemplateDataUploadLog(username=d1, bldgid=d2)
		d.save()

	elif option == 2:
		d = TemplateDataUploadLog.objects.filter(username=d1).delete()

