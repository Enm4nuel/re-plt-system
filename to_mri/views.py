from django.shortcuts import render
from django.http import HttpResponse

from datos.views import *
from datos.models import *

from plantillas.views import *
from plantillas.models import *

from .models import *

# Create your views here.

server = '172.24.1.39'
database = 'FACTURA'
username = 'Data_Editor'
password = 'jr03124300'

def formatear_data(request):

	cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM VINCH")
	row = cursor.fetchall()

	for i in range(len(row)):
		print(row[i])

	return HttpResponse("formatear_data")
"""
	td = TemplateData.objects.all()
	t = Template.object.all()
	tl = TemplateLog.objects.order_by('-date')[:1]

	# no cambian
	cmbatch = tl.batch
	trandate = tl.invoice_date # para arreglar

	item = 0


	# Guardar datos en tabla "tomri_data"
	for d in data:
		for i in t:
			inccat = ""
			for k, v in d.fields.items():
				for k2, v2 in i.fields.items():
					if k == v2:
						inccat = k2
			tm = ToMri(
				cmbatch = cmbatch,
				item = item,
				bldgid = d.bldgid,
				leasid = d.leasid,
				trandate = trandate,
				inccat = inccat,
				# srccode = CH
				descrptn = "",
				tranamt = "",
				# taxitem = N
				rtaxgrpid = "",
				# department = @
				currcode = ""
				# bcurcode = DOP 
			)
			tm.save()
			###
			item += 1


	# Visualizar datos por edificio
	for d in data:
		for k,v in d.fields.items():
			if v is not None and v > 0 and v != "" and v != "0" and v != "0.0" and v != "0.00":
				print("------------------------------------------")
				print("-", d.bldgid, "|", d.leasid, ", Llave: ", k, "|", "Valor: ", v)
				print("------------------------------------------")

	return HttpResponse("formatear_data")
	"""