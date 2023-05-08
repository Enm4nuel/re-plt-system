from django.shortcuts import render
from django.http import HttpResponse

from datos.views import *
from datos.models import *

from .models import *

# Create your views here.

def formatear_data(request):

	data = TemplateData.objects.all()

	buildings = []

	cmbatch
	item = 0

	# Extraer todos los edificios
	for d in data:
		if d.bldgid not in buildings:
			buildings.append(d.bldgid)

	# Guardar datos en tabla "tomri_data"
	for d in data:
		tm = ToMri(
			cmbatch
			item = item
			bldgid = d.bldgid
			leasid = d.leasid
			trandate
			inccat = 
			srccode
			descrptn
			tranamt
			taxitem
			rtaxgrpid
			department
			currcode
			bcurcode
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