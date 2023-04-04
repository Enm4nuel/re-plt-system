from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponseRedirect

import os
import pathlib
import pandas as pd
import numpy as np

from openpyxl import load_workbook

from plantillas.models import Plantilla
from plantillas.views import cargar_datos
from datos.views import visualizar_data, agregar_Datosp, agregar_LogDatosp
from datos.models import Datosp, LogDatosP

#columnas2 = [] 
#filtro = []

def su_test(user):
	return user.is_superuser

@login_required(login_url='/admin/')
def home(request):

	if request.user.is_authenticated:
		print("User is logged in :)")
		print(f"Username --> {request.user.username}")
	else:
		print("User is not logged in :(")

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/home.html')

@login_required(login_url='/admin/')
def descargar_csv(request):

	if request.method == 'POST':
		
		if 'edificio' in request.POST:
			edificio = request.POST.get('edificio')
			moneda = request.POST.get('moneda')

			cargar_datos(edificio, moneda)

			return HttpResponseRedirect('/')
		
	else:
		print("No has hecho ningun POST")

	edificios = []
	monedas = []

	e = Plantilla.objects.all()
	for i in e:
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
		

			columnas = []
			for col in sheet.iter_cols(min_col=2):
				columnas.append(col[0].value)

			data = []
			filtro = ""

			"""
			for row in sheet.iter_rows(min_row=2):

				data2 = {}

				for c in range(4,len(columnas)):
					data2[str(columnas[c])] = row[c+1].value

					
				data.append([row[1].value, row[2].value, row[3].value, row[4].value, data2])

				filtro = row[2].value
			"""

			for row in sheet.iter_rows(min_row=2):

				data2 = []

				for c in range(4,len(columnas)):
					data2.append(row[c+1].value)

					
				data.append([row[1].value, row[2].value, row[3].value, row[4].value, data2])

				filtro = row[2].value

			totales = []
			#for i in data:
				#for j in i[4]:
					#print(j)

			
			a.filename = file.name
			a.cols = columnas
			a.data = data
			a.filtro = filtro
			a.totales = totales
			

			return HttpResponseRedirect('/subir_archivo/confirmar/'+ file.name)

	else:
		print("No has hecho ningun POST")

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo.html')




"""
@login_required(login_url='/admin/')
def subir_archivo(request):

	if request.method == 'POST':

		if 'file' in request.FILES:

			file = request.FILES['file']
			workbook = load_workbook(file)
			sheet = workbook.active
			
			visualizar_data(request, file.name, workbook)

			columnas2.clear()
			for col in sheet.iter_cols(min_col=2):
				columnas2.append(col[0].value)

			for row in sheet.iter_rows(min_row=2):
				filtro.append(row[2].value)
				break
				#rows.append([row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value, row[6].value, row[7].value])

			return HttpResponseRedirect('/subir_archivo/confirmar/'+ file.name)

	else:
		print("No has hecho ningun POST")

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo.html')
"""




@login_required(login_url='/admin/')
def subir_archivo_confirmar(request, filename):

	#d = Datosp.objects.filter(bldgid__contains=filtro[0])
	d = []
	print(a.filename)

	#return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columnas': columnas2, 'data': d, 'name': filename})
	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columnas': a.cols, 'data': a.data, 'name': a.filename})

@login_required(login_url='/admin/')
def subir_archivo_confirmar_cc(request):

	for row in a.data:
		if Datosp.objects.filter(bldgid=row[1]):
			Datosp.objects.filter(bldgid=row[1]).delete()
			print("listo")
		else:
			print("no existe")
		break
	
	limit = 4

	for row in a.data:
		data = {}
		for c in range(limit,len(a.cols)):
			data[str(a.cols[c])] = row[limit][c-limit]
		agregar_Datosp(row[0], row[1], row[2], row[3], data)
		print("Se han agregado los datos nuevos a ", row[1])

	agregar_LogDatosp(request.user.username, a.filtro, False)

	"""data = LogDatosP.objects.get(building__contains=filtro[0])
	data.real = True
	data.save()
	print(data)
	print("subir_archivo_confirmar_cc sirve")"""
	return HttpResponseRedirect("/")

@login_required(login_url='/admin/')
def subir_archivo_confirmar_dc(request):

	a.filename = ""
	a.cols = []
	a.data = []
	a.filtro = ""
	a.totales = []

	print("imprimiendo objeto de nombre: a \n", a)
	return HttpResponseRedirect("/")




@login_required(login_url='/admin/')
@user_passes_test(su_test)
def validar_datos(request):
	
	data = Datosp.objects.all()
	filtros = LogDatosP.objects.all()
	#filtros = []

	#for f in filtro:
		#filtros.append(f.building)

	#print(filtros)


	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/validar_datos.html', context={'data': data, 'filtros': filtros})





@login_required(login_url='/admin/')
@user_passes_test(su_test)
def postear_datos(request):
	
	data = LogDatosP.objects.all()

	plt = []
	p = Plantilla.objects.all()
	for i in p:
		if i not in plt:
			print(i)
			plt.append(i)
	print(plt)

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


"""
{% for i in data %}
					<tr>	
						<td> {{i.leasid}} </td>
						<td> {{i.bldgid}} </td>
						<td> {{i.suitid}} </td>
						<td> {{i.occpname}} </td>
						{% for k,v in i.values.items %}
							<td> {{"g"}} </td>
						{% endfor %}
					</tr>
				{% endfor %}
"""