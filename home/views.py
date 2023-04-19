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
				return redirect("/subir_archivo/confirmar/")
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
			uploadDataToDb(request, workbook)

			return redirect('/subir_archivo/confirmar/')

	else:
		print("No has hecho ningun POST")

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo.html')

@login_required(login_url='/admin/')
def subir_archivo_confirmar(request):

	filtro = TemplateDataUploadLog.objects.filter(username=request.user.username)
	filtr = ""
	for f in filtro:
		filtr = f.bldgid

	data = TemplateData.objects.filter(bldgid__contains=filtr)
	
	columns = ["LEASID", "BLDGID", "SUITID", "OCCPNAME"]
	for d in data:
		for k, v in d.fields.items():
			if k not in columns:
				columns.append(k)	

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/subir_archivo_confirmar.html', context={'columns': columns, 'data': data, 'filtr': filtr, 'name': 'plantilla'})

@login_required(login_url='/admin/')
def subir_archivo_confirmar_cc(request, bldgid):

	templateDataLog(1, request.user.username, bldgid, True, False)
	templateDataUploadLog(2, request.user.username, "")

	return redirect("/")

@login_required(login_url='/admin/')
def subir_archivo_confirmar_dc(request, bldgid):

	deleteData(bldgid)
	templateDataUploadLog(2, request.user.username, "")

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

	d = TemplateDataLog.objects.get(id=id)
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
