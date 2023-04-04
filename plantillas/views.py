from django.shortcuts import render, redirect
import os
import pathlib
import pandas as pd
import numpy as np

import openpyxl

from .models import Plantilla

import pyodbc

server = '172.24.1.39'
database = 'FACTURA'
username = 'Data_Editor'
password = 'jr03124300'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.

def cargar_datos(edificio, moneda):

	cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
	print(edificio)
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM Vpfacturacion WHERE BLDGID = '%s'" % edificio)
	row = cursor.fetchall()

	print("funcion cargar datos bien")

	leasid = []
	bldgid = []
	suitid = []
	occpname = []
	descripciones = []

	for i in range(len(row)):
		leasid.append(row[i][0])
		bldgid.append(row[i][1])
		suitid.append(row[i][2])
		occpname.append(row[i][3])

	p = Plantilla.objects.all()
	for i in p:
		if i.bldgid == edificio and i.currcode == moneda:
			descripciones.append(i.descrptn)

	generar_plantilla(moneda, edificio, descripciones, leasid, bldgid, suitid, occpname)
	cursor.close()

	return 0

"""
def cargar_datos(edificio, moneda):

	cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)

	if edificio == "T-CAM":

		cursor = cnxn.cursor()
		cursor.execute("SELECT * FROM Vpfacturacion WHERE BLDGID='T-CAM' ")
		row = cursor.fetchall()

		leasid = []
		bldgid = []
		suitid = []
		occpname = []
		descripciones = []

		for i in range(len(row)):
			leasid.append(row[i][0])
			bldgid.append(row[i][1])
			suitid.append(row[i][2])
			occpname.append(row[i][3])

		p = Plantilla.objects.all()
		for i in p:
			if i.bldgid == 'T-CAM':
				descripciones.append(i.descrptn)

		print(descripciones)
		generar_plantilla(moneda, edificio, descripciones, leasid, bldgid, suitid, occpname)
		cursor.close()

	elif edificio == "BM-SDC":

		cursor = cnxn.cursor()
		cursor.execute("SELECT * FROM Vpfacturacion WHERE BLDGID='BM-SDC'")
		row = cursor.fetchall()

		leasid = []
		bldgid = []
		suitid = []
		occpname = []
		descripciones = []

		for i in range(len(row)):
			leasid.append(row[i][0])
			bldgid.append(row[i][1])
			suitid.append(row[i][2])
			occpname.append(row[i][3])

		p = Plantilla.objects.all()
		for i in p:
			if i.bldgid == 'BM-SDC':
				descripciones.append(i.descrptn)
				print(i.descrptn)

		print(descripciones)
		generar_plantilla(moneda, edificio, descripciones, leasid, bldgid, suitid, occpname)
		cursor.close()

	elif edificio == "BM-PCC":
		
		cursor = cnxn.cursor()
		cursor.execute("SELECT * FROM Vpfacturacion WHERE BLDGID='BM-PCC'")
		row = cursor.fetchall()

		leasid = []
		bldgid = []
		suitid = []
		occpname = []
		descripciones = []

		for i in range(len(row)):
			leasid.append(row[i][0])
			bldgid.append(row[i][1])
			suitid.append(row[i][2])
			occpname.append(row[i][3])

		p = Plantilla.objects.all()
		for i in p:
			if i.bldgid == 'BM-PCC':
				descripciones.append(i.descrptn)
				print(i.descrptn)

		print(descripciones)
		generar_plantilla(moneda, edificio, descripciones, leasid, bldgid, suitid, occpname)
		cursor.close()
	
	else:
		print("No se selecciono ningun edificio")

	return 0
"""

def generar_plantilla(moneda, edificio, index = [], leasid = [], bldgid = [], suitid = [], occpname = []):
	d = {'LEASID': leasid, 'BLDGID': bldgid, 'SUITID': suitid, 'OCCPNAME': occpname}
	for i in range(len(index)):
		d[str(index[i])] = ""
	df = pd.DataFrame(data=d)
	df.to_excel("Plantilla" + edificio + "_" + moneda + ".xlsx")


def modificar_plantillas(request):

	if request.method == 'POST':

		if 'descrptn_input' in request.POST:
			try:
				
				bldgid = str(request.POST.get('bldgid_select'))
				currcode = str(request.POST.get('currcode_select'))
				inccat = str(request.POST.get('inccat_input'))
				descrptn = str(request.POST.get('descrptn_input'))


				p = Plantilla(bldgid=bldgid, currcode=currcode, inccat=inccat, descrptn=descrptn)
				p.save()

				print("El campo nuevo se ha guardado correctamente!!")

			except NameError:
				print("No se pudo guardar el campo nuevo!", NameError)

	else:
		print("No se ha generado ningun POST")


	data = Plantilla.objects.all()

	return render(request, 'C:/Users/Leonor Fischer/Documents/re-sys-main/plantillas/templates/modificar_plantillas.html', context={'data': data})

def modificar_plantillas_eliminar(request, id):
	
	p = Plantilla.objects.get(id=id)
	p.delete()

	return redirect('/plantillas/modificar_plantillas')

def modificar_plantillas_editar(request, id):

	if request.method == 'POST':
		pass

	return redirect('/plantillas/modificar_plantillas')