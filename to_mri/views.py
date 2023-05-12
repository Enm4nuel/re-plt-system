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

from django.contrib import messages


def formatear_data(request, bldgid):


    # Extraer data de vista 'inch' para validaciones de inccat
    dm = DbManage()
    inch = dm.connect2()

    # Filtrar y extraer data con lo que se va a trabajar
    template_data = TemplateData.objects.filter(bldgid__contains=bldgid)
    cmbatch = template_data[0].cmbatch  # Batch que se usara en la exportacion del consolidado
    #  rate = template_data[0].rate  # taza que se usara en la exportacion del consolidado

    # Extraemos la data de esta tabla para validar si los inccat evaluados existen en el sistema
    template = Template.objects.all()

    # Filtramos por batch y obtenemos el trandate del cons
    template_log = TemplateLog.objects.all().filter(batch=cmbatch)
    trandate = template_log[0].invoice_date
    rate = template_log[0].rate
    
    #
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
            for i in inch:
                if i[0] == inccat:
                    rtax = i[1]
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
    

    # Response
    return HttpResponse("formatear_data")

"""
    try:
        # Extraer data de vista 'inch' para validaciones de inccat
        dm = DbManage()
        inch = dm.connect2()

        # Filtrar y extraer data con lo que se va a trabajar
        template_data = TemplateData.objects.filter(bldgid__contains=bldgid)
        cmbatch = template_data[0].cmbatch  # Batch que se usara en la exportacion del consolidado
        #  rate = template_data[0].rate  # taza que se usara en la exportacion del consolidado

        # Extraemos la data de esta tabla para validar si los inccat evaluados existen en el sistema
        template = Template.objects.all()

        # Filtramos por batch y obtenemos el trandate del cons
        template_log = TemplateLog.objects.all().filter(batch=cmbatch)
        trandate = template_log[0].invoice_date
        rate = template_log[0].rate
        
        #
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
                for i in inch:
                    if i[0] == inccat:
                        rtax = i[1]
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
        

        # Response
        return HttpResponse("formatear_data")
    except:
        pass
    else:
        True
"""


def export_excel(request, bldgid):
    formatear_data(request, bldgid)
    generar_consolidado(bldgid)

    # Eliminamos la data de 'template_data' luego de haberla exportado
    TemplateData.objects.filter(bldgid__contains=bldgid).delete()

    # Eliminamos la data de 'tomri_data' luego de haberla exportado
    #ToMri.objects.all().delete()

    # --
    messages.success(request, "Data exportada!")

    return redirect("/data_post/")


def generar_consolidado(bldgid):

    # Extraer data de la tabla 'tomri_data' y convertirla a DataFrame
    data = ToMri.objects.all()
    df = pd.DataFrame(list(data.values()))

    # Para almacenar y convertir a mayusculas, la fila que contiene el nombre de las columnas
    columns = []

    # Obtener columnas en mayusculas
    for row in dataframe_to_rows(df, index=False, header=True):
        for r in row:
            columns.append(str(r.upper()))
        break

    # Para separar la primera linea o fila de las demas
    i = 0

    # Declarar el libro de trabajo y la hoja actual (o activa)
    workbook = Workbook()
    worksheet = workbook.active
    # ------------------------------------------------------ #
    
    # Algoritmo de crear excel
    for row in dataframe_to_rows(df, index=False, header=True):
        if i == 0:
            worksheet.append(columns)
            i = 1
        else:  # Aqui sigue llenando el excel con normalidad
            if bldgid == row[2]:
                # Formatear fecha
                fecha = row[4]
                trandate = fecha.strftime('%m/%d/%Y')
                row[4] = trandate
                # --------------- #
                worksheet.append(row)
    # ------------------------------------------------------ #

    # Guardamos el excel
    workbook.save("Consolidado_"+bldgid+".xlsx")
        


"""
def formatear_data(request, bldgid):
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
def export_excel(request, bldgid):
    formatear_data(request, bldgid)
    generar_consolidado()
    # Eliminamos la data de 'template_data' luego de haberla exportado
    TemplateData.objects.all().delete()
    # Eliminamos la data de 'tomri_data' luego de haberla exportado
    #ToMri.objects.all().delete()

    return redirect("/data_post/")
def generar_consolidado():

    # variable que almacena los edificios
    buildings = []

    # Extraer edificios
    for tm in ToMri.objects.values_list('bldgid', flat=True):
        if tm not in buildings:
            buildings.append(tm)

    # Extraer data de la tabla 'tomri_data' y convertirla a DataFrame
    data = ToMri.objects.all()
    df = pd.DataFrame(list(data.values()))

    # Para almacenar y convertir a mayusculas, la fila que contiene el nombre de las columnas
    columns = []

    # Obtener columnas en mayusculas
    for row in dataframe_to_rows(df, index=False, header=True):
        for r in row:
            columns.append(str(r.upper()))
        break

    # Para separar la primera linea o fila de las demas
    i = 0

    # Rellenar el excel con la data extraida
    for b in buildings:
        # Declarar el libro de trabajo y la hoja actual (o activa)
        workbook = Workbook()
        worksheet = workbook.active
        # ------------------------------------------------------ #
        # Algoritmo de crear excel
        for row in dataframe_to_rows(df, index=False, header=True):
            if i == 0:
                worksheet.append(columns)
                i = 1
            else:  # Aqui sigue llenando el excel con normalidad
                if b == row[2]:
                    worksheet.append(row)
        # ------------------------------------------------------ #
        # Guardamos el excel
        workbook.save("Consolidado_"+b+".xlsx")
        i = 0
"""