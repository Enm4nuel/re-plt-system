from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Datosp, LogDatosP

def index():
	print("Estas en datos")


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

def agregar_Datosp(d1, d2, d3, d4, d5):
	d = Datosp(leasid=d1, bldgid=d2, suitid=d3, occpname=d4, values=d5)
	d.save()

def agregar_LogDatosp(d1, d2, d3):

	if LogDatosP.objects.filter(building=d2).exists():
		d = LogDatosP.objects.get(building=d2)
		d.username = d1
		d.building = d2
		d.real = d3
		d.created = timezone.now()
		d.save()
	else:
		d = LogDatosP(username=d1, building=d2, real=d3, created=timezone.now())
		d.save()

	print("log de datos cargados, se ha ejecutado correctamente")


"""
def agregar_DatosTcam(d1, d2, d3, d4, d5):
	d = DatosTcam(leasid=d1, bldgid=d2, suitid=d3, occpname=d4, values=d5)
	d.save()

def agregar_DatosBmSdc(d1, d2, d3, d4, d5):
	d = DatosBmSdc(leasid=d1, bldgid=d2, suitid=d3, occpname=d4, values=d5)
	d.save()

def agregar_DatosBmPcc(d1, d2, d3, d4, d5):
	d = DatosBmPcc(leasid=d1, bldgid=d2, suitid=d3, occpname=d4, values=d5)
	d.save()

def probar_f1(d1, d2, d3, d4, d5):
	d = Datos(bldgid=d1, leasid=d2, suitid=d3, descrptn=d4, value=d5)
	d.save()

def probar_f2(d0, d1, d2, d3, d4, d5):
	d = Datos.objects.get(pk=d0)
	d.bldgid = d1
	d.leasid = d2
	d.suitid = d3
	d.descrptn = d4
	d.value = d5
	d.save()
"""