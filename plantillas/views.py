from django.shortcuts import render, redirect
import os
import pandas as pd
import numpy as np

from openpyxl import Workbook
from openpyxl.styles import Font, Color

from .models import Template, TemplateLog, TemplateMonthlyCfgLog, TemplateMonthlyCfg

import pyodbc

server = '172.24.1.39'
database = 'FACTURA'
username = 'Data_Editor'
password = 'jr03124300'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.

def loadData(building, coin):

	cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM Vpfacturacion WHERE BLDGID = '%s'" % building)
	row = cursor.fetchall()

	leasid = []
	bldgid = []
	suitid = []
	occpname = []
	descripciones = []

	for i in range(len(row)):
		leasid.append(row[i][0])
		if "T-CAM" in row[i][1]:
			b = row[i][1].split(" ")
			bldgid.append(b[0])
		else:
			bldgid.append(row[i][1])
		suitid.append(row[i][2])
		occpname.append(row[i][3])

	t = Template.objects.all()
	print(t)
	for i in t:
		for k, v in i.fields.items():
			if i.bldgid == building and i.currcode == coin:
				descripciones.append(v)

	generar_plantilla(coin, building, descripciones, leasid, bldgid, suitid, occpname)
	cursor.close()

	return 0

def generar_plantilla(coin, building, index = [], leasid = [], bldgid = [], suitid = [], occpname = []):
	d = {'LEASID': leasid, 'BLDGID': bldgid, 'SUITID': suitid, 'OCCPNAME': occpname}
	for i in range(len(index)):
		d[str(index[i])] = ""
	df = pd.DataFrame(data=d)
	df.to_excel("Plantilla" + building + "_" + coin + ".xlsx")

	TemplateLog.objects.create(bldgid=building, batch=3435)


def prueba_generar_plantilla(moneda, edificio, index = [], leasid = [], bldgid = [], suitid = [], occpname = []):

	wb = Workbook()
	ws = wb.active

	ws['A2'] = "Tasa"
	ws['B2'] = 57.99
	ws['A3'] = ""

	let = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

	headers = ['LEASID', 'BLDGID', 'SUITID', 'OCCPNAME']

	for i in range(len(index)):
		headers.append(index[i])
	
	ws.append(headers)

	for i in range(len(leasid)):
		ws.append([leasid[i], bldgid[i], suitid[i], occpname[i]])
		

	# ESTILOS
	TITULO = Font(bold=True)

	row4 = ws.row_dimensions[4]
	row4.font = TITULO

	row1 = ws.row_dimensions[4]
	row1.font = Font()


	#ws['1'].font = Font(bold=True)

	wb.save("Plantilla" + edificio + "_" + moneda + ".xlsx")


"""
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

	return redirect('/plantillas/modificar_plantillas')"""