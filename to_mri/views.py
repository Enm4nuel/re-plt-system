from django.http import HttpResponse

import pandas as pd
import numpy as np

from datos.views import *
from datos.models import *

from plantillas.views import *
from plantillas.models import *

from .models import *

from db.db_manage import *

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font


def formatear_data(request):
    dm = DbManage()
    row = dm.connect2()

    template_data = TemplateData.objects.all()
    template = Template.objects.all()
    template_log = TemplateLog.objects.order_by("-created")[:1]

    # no cambian
    cmbatch = template_log[0].batch
    trandate = template_log[0].invoice_date  # para arreglar
    rate = template_log[0].rate

    item = 1

    # Guardar datos en tabla "tomri_data"
    for td in template_data:
        for t in template:
            inccat = ""
            currcode = ""
            rtax = ""
            tranamt = 0.0
            descrptn = ""
            for k, v in td.fields.items():
                if k == t.descrptn_name:
                    inccat = t.inccat
                    currcode = t.currcode
                    if v != 0:
                        tranamt = (float(v)) / (float(rate))
                    descrptn = t.descrptn
            for r in row:
                if r[0] == inccat:
                    rtax = r[1]
            if tranamt != 0 and tranamt != 0.0:
                tm = ToMri(
                    cmbatch=cmbatch,
                    item=item,
                    bldgid=td.bldgid,
                    leasid=td.leasid,
                    trandate=trandate,
                    inccat=inccat,
                    # srccode = CH
                    descrptn=descrptn,
                    tranamt=tranamt,
                    # taxitem = N
                    rtaxgrpid=rtax,
                    # department = @
                    currcode=currcode
                    # bcurcode = DOP
                )
                tm.save()
                ###
                item += 1
            else:
                pass

    data = ToMri.objects.all()

    # Visualizar datos por edificio
    for d in data:
        print("------------------------------------------")
        print(
            "-",
            d.bldgid,
            "|",
            d.leasid,
            ", Description: ",
            d.descrptn,
            "|",
            "Valor: ",
            d.tranamt,
        )
        print("------------------------------------------")

    # Generar consolidado
    #generar_consolidado(data)

    # Response
    return HttpResponse("formatear_data")


def export_excel(request):
    generar_consolidado()

    return redirect("/data_post/")


def generar_consolidado():
    data = ToMri.objects.all()
    df = pd.DataFrame(list(data.values()))

    # Escribir el DataFrame en el archivo de Excel
    workbook = Workbook()
    worksheet = workbook.active

    for row in dataframe_to_rows(df, index=False, header=True):
        worksheet.append(row)

    workbook.save("my_table.xlsx")
    #ToMri.objects.all().delete()


"""
	rows = ToMri.objects.all()

	for row in range(len(rows)):


	tm = ToMri()
	columns = tm.getColumns()
	d = {}

	print(columns)

	for c in range(len(columns)):
		d[str(columns[c])] = 10

	#for r in rows:
		#for c in range(len(columns)):
			#data[columns[c]] = 

	#print(data)
	df = pd.DataFrame(data=d)
	df.to_excel("Consolidado"+".xlsx")
"""
