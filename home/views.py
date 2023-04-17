from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

import os
import pathlib
import pandas as pd
import numpy as np

import asyncio

from openpyxl import load_workbook

from plantillas.models import *
from plantillas.views import *

from datos.views import *
from datos.models import *

# Global var
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/home"

def su_test(user):
	return user.is_superuser

@login_required(login_url='/admin/')
def home(request):

	if TemplateDataUploadLog.objects.filter(username=request.user.username).exists():
		d = TemplateDataUploadLog.objects.get(username=request.user.username)
		if request.user.is_authenticated:
			if d.active == True:
				messages.warning(request, "Tienes una plantilla precargada con informacion sin validar!")
				return redirect("/subir_archivo/confirmar/"+d.bldgid)
	else:
		print("User is not logged in :(")

	return render(request, '{}/templates/home.html'.format(base_dir), context={"message": messages})

@login_required(login_url='/admin/')
def descargar_csv(request):

	if request.method == 'POST':
		
		if 'edificio' in request.POST:
			building = request.POST.get('edificio')
			coin = request.POST.get('moneda')
			batch = request.POST.get('batch')

			loadData(building, coin, batch, request.user.username)

			messages.success(request, "Se ha descargado la plantilla con exito!")

			return redirect('/')
		
	else:
		return 0

	edificios = []
	monedas = []

	t = Template.objects.all()
	for i in t:
		if i.bldgid not in edificios:
			edificios.append(i.bldgid)
		if i.currcode not in monedas:
			monedas.append(i.currcode)
	
	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/descargar_plantilla.html', context={'edificios': edificios, 'monedas': monedas})

@login_required(login_url='/admin/')
def subir_archivo(request):

	if request.method == 'POST':

		if 'file' in request.FILES:

			file = request.FILES['file']
			workbook = load_workbook(file)
			sheet = workbook.active
		
			columns = []
			for col in sheet.iter_cols(min_col=2):
				columns.append(col[0].value)

			data = []
			filtr = ""

			for row in sheet.iter_rows(min_row=2):

				data2 = []

				for c in range(4,len(columnas)):
					data2.append(row[c+1].value)

				data.append([row[1].value, row[2].value, row[3].value, row[4].value, data2])
				filtro = str(row[2].value)

			
			a.filename = file.name
			a.cols = columns
			a.data = data
			a.filtro = filtr
			a.totales = []


			templateDataUploadLog(1, request.user.username, filtro)

			return redirect('/subir_archivo/confirmar/'+ file.name)

	else:
		print("No has hecho ningun POST")

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo.html')

@login_required(login_url='/admin/')
def subir_archivo_confirmar(request, filename):

	print(a.filename)

	#return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columnas': columnas2, 'data': d, 'name': filename})
	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columnas': a.cols, 'data': a.data, 'name': a.filename})

@login_required(login_url='/admin/')
def subir_archivo_confirmar2(request, building):

	#return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columnas': columnas2, 'data': d, 'name': filename})
	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columnas': a.cols, 'data': a.data, 'name': a.filename})

@login_required(login_url='/admin/')
def subir_archivo_confirmar_cc(request):

	for row in a.data:
		if TemplateData.objects.filter(bldgid=row[1]):
			TemplateData.objects.filter(bldgid=row[1]).delete()
			print("listo")
		else:
			print("no existe")
		break
	
	limit = 4

	for row in a.data:
		data = {}
		for c in range(limit,len(a.cols)):
			data[str(a.cols[c])] = row[limit][c-limit]
		templateData(1, row[0], row[1], row[2], row[3], data)
		print("Se han agregado los datos nuevos a ", row[1])

	# para crear un registro de la confirmacion de plantilla
	#templateDataLog(1, request.user.username, a.filtro, True, False)

	# para borrar el registro de subida de una plantilla
	templateDataUploadLog(2, request.user.username, "")

	return redirect("/")

@login_required(login_url='/admin/')
def subir_archivo_confirmar_dc(request):

	a.filename = ""
	a.cols = []
	a.data = []
	a.filtro = ""
	a.totales = []

	templateDataUploadLog(2, request.user.username, "")

	print("imprimiendo objeto de nombre: a \n", a)
	return redirect("/")


@login_required(login_url='/admin/')
@user_passes_test(su_test)
def validar_datos(request):
	
	data = TemplateData.objects.all()
	filtros = TemplateDataLog.objects.all()

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/validar_datos.html', context={'data': data, 'filtros': filtros})

@login_required(login_url='/admin/')
@user_passes_test(su_test)
def validar_datos_confirmar(request, id):

	d = TemplateData.objects.get(id=id)
	if d.second_validation == True:
		templateDataLog(2, id, False, "", "", "")
	else:
		templateDataLog(2, id, True, "", "", "")

	return HttpResponseRedirect("/validar_datos/")



@login_required(login_url='/admin/')
@user_passes_test(su_test)
def postear_datos(request):
	
	data = TemplateDataLog.objects.all().order_by('created').values()

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/postear_datos.html', context={'data': data})



class Archivo:
	def __init__(self, filename, cols, data, filtro, totales):
		self.filename = filename
		self.cols = cols
		self.data = data
		self.filtro = filtro
		self.totales = totales

	def add(self, dato):
		self.data.append(dato)

a = Archivo("", [], [], "", [])
