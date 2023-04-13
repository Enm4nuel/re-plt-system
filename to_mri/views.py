from django.shortcuts import render
from django.http import HttpResponse
from datos.models import Datosp, LogDatosP, LogSubirDatosP

# Create your views here.

def formatear_data(request):

	data = Datosp.objects.all()

	buildings = []

	# Extraer todos los edificios
	for d in data:
		if d.bldgid not in buildings:
			buildings.append(d.bldgid)

	# Visualizar datos por edificio
	for d in data:
		for k,v in d.values.items():
			print("------------------------------------------")
			print(d.leasid, "- Llave: ", k, "|", "Valor: ", v)
			print("------------------------------------------")

	print(buildings)

	return HttpResponse("formatear_data")