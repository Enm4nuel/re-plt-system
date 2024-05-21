from django.shortcuts import render, redirect
from django.template import Context, Template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
<<<<<<< HEAD
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db import IntegrityError
from http import HTTPStatus
=======
from django.contrib import messages
from django.db import IntegrityError
>>>>>>> master

import os

from openpyxl import load_workbook

from re_sys.settings import BASE_DIR

from plantillas.models import *
from plantillas.views import *

from datos.views import *
from datos.models import *

def su_test(user):
	return user.is_superuser


<<<<<<< HEAD
@login_required(login_url='/admin/')
=======
>>>>>>> master
def home(request):

	if TemplateDataUploadLog.objects.filter(username=request.user.username).exists():
		d = TemplateDataUploadLog.objects.get(username=request.user.username)
		if request.user.is_authenticated:
			if d.active == True:
				messages.warning(request, "Tienes una plantilla precargada con informacion sin validar!")
				return redirect("/csv_upload/confirm/")
	else:
		print("User is not logged in :(")

<<<<<<< HEAD
	return render(request, BASE_DIR+'/home/templates/home.html', context={"message": messages})


@login_required(login_url='/admin/')
=======
	return render(request, 'home.html', context={"message": messages})


>>>>>>> master
def csv_download(request):

	try:
		if request.method == 'POST':
		
			if 'edificio' in request.POST:
				building = request.POST.get('edificio')
				coin = request.POST.get('moneda')
				batch = request.POST.get('batch')
				rate = request.POST.get('rate')

				loadData(building, coin, batch, rate, request.user.username)

				messages.success(request, "Se ha descargado la plantilla con exito!")

				response = redirect("/")
				response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
				return response
			else:
				pass
		else:
			return 0
	except IntegrityError as err:
<<<<<<< HEAD
		return render(request, BASE_DIR+"/home/templates/handler_error.html", {"type": err.__type__, "message": err.__cause__, "detalles": "detalles"})
=======
		return render(request, "handler_error.html", {"type": err.__type__, "message": err.__cause__, "detalles": "detalles"})
>>>>>>> master

	edificios = []
	monedas = []

	t = Template.objects.all()
	for i in t:
		if i.bldgid not in edificios:
			edificios.append(i.bldgid)
		if i.currcode not in monedas:
			monedas.append(i.currcode)
	
<<<<<<< HEAD
	return render(request, BASE_DIR+'/home/templates/csv_download.html', context={'edificios': edificios, 'monedas' :monedas})


@login_required(login_url='/admin/')
=======
	return render(request, 'csv_download.html', context={'edificios': edificios, 'monedas' :monedas})


>>>>>>> master
def csv_upload(request):

	if request.method == 'POST':

		if 'file' in request.FILES:

			file = request.FILES['file']
			workbook = load_workbook(file)
			rtn = uploadDataToDb(request, workbook)

			if rtn == False:
				print("Se produjo un error")
				messages.error(request, "Se ha producido un error al intentar cargar la plantilla!")
				response = redirect('/')
				response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
				return response
			else:
				response = redirect('/csv_upload/confirm/')
				response['Cache-Control'] = 'no-cache'
				return response

	else:
		print("No has hecho ningun POST")

<<<<<<< HEAD
	return render(request, BASE_DIR+'/home/templates/csv_upload.html')

@login_required(login_url='/admin/')
=======
	return render(request, 'csv_upload.html')


>>>>>>> master
def csv_upload_confirm(request):

	filtro = TemplateDataUploadLog.objects.filter(username=request.user.username)
	filtr = ""
	for f in filtro:
		try:
			filtr = f.bldgid
		except:
			print("No se pudo extraer la informacion")
			response = redirect('/csv_upload/')
			response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
			return response

	# para nombrar el caption o legend de la tabla
	name = "Plantilla_"+filtr

	data = TemplateData.objects.filter(bldgid__contains=filtr)
	
	columns = ["LEASID", "BLDGID", "SUITID", "OCCPNAME"]
	totals = {}

	c = len(data)
	rate = getRate()

	# Extraer columnas y totales por columna
	for d in data:
		for k, v in d.fields.items():
			if k not in columns:
				columns.append(k)
				totals["{}".format(k)] = v*c

<<<<<<< HEAD
	return render(request, BASE_DIR+'/home/templates/csv_upload_confirm.html', context={'columns': columns, 'data': data, 'totals': totals, 'filtr': filtr, 'name': name})

@login_required(login_url='/admin/')
=======
	return render(request, 'csv_upload_confirm.html', context={'columns': columns, 'data': data, 'totals': totals, 'filtr': filtr, 'name': name})


>>>>>>> master
def csv_upload_confirm_cc(request, bldgid):

	templateDataLog(1, request.user.username, bldgid, True, False)
	templateDataUploadLog(2, request.user.username, "")

	response = redirect("/")
	response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

<<<<<<< HEAD
@login_required(login_url='/admin/')
=======

>>>>>>> master
def csv_upload_confirm_dc(request, bldgid):

	deleteData(bldgid)
	templateDataUploadLog(2, request.user.username, "")

	response = redirect("/")
	response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response


<<<<<<< HEAD
@login_required(login_url='/admin/')
=======
>>>>>>> master
@user_passes_test(su_test)
def data_validate(request):
	
	data = TemplateData.objects.all()
	filtros = TemplateDataLog.objects.all()

<<<<<<< HEAD
	return render(request, BASE_DIR+'/home/templates/data_validate.html', context={'data': data, 'filtros': filtros})

@login_required(login_url='/admin/')
=======
	return render(request, 'data_validate.html', context={'data': data, 'filtros': filtros})


>>>>>>> master
@user_passes_test(su_test)
def data_validate_confirm(request, id):

	d = TemplateDataLog.objects.get(id=id)
	if d.second_validation == True:
		templateDataLog(2, id, False, "", "")
	else:
		templateDataLog(2, id, True, "", "")

	return redirect("/data_validate/")


<<<<<<< HEAD
@login_required(login_url='/admin/')
=======
>>>>>>> master
@user_passes_test(su_test)
def data_post(request):
	
	data = TemplateDataLog.objects.all().order_by('created').values()

<<<<<<< HEAD
	return render(request, BASE_DIR+'/home/templates/data_post.html', context={'data': data})



# Vistas para manejo de errores
def handler_404(request, exception):
	return render(request, BASE_DIR+'/home/templates/handle_errors/404.html')
=======
	return render(request, 'data_post.html', context={'data': data})
>>>>>>> master
