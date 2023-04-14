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
			if v is not None and v != 0 and v != "" and v != "0" and v != "0.0" and v != "0.00":
				print("------------------------------------------")
				print(d.leasid, "- Llave: ", k, "|", "Valor: ", v)
				print("------------------------------------------")

	print(buildings)

	return HttpResponse("formatear_data")