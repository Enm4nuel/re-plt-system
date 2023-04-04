from django.http import HttpResponse
from django.template import Context, Template
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

import os
import pathlib
import pandas as pd
import numpy as np
import webbrowser

from .forms import NameForm

def leerCSV(request):

    uplfile = request.FILES['file'].readlines()

    prt = []
    prt2 = []

    for file in uplfile:
        prt.append('{}'.format(file.strip()))

    for i in prt:
        prt2.append(i.split(','))



    
    print(prt2[3121][1])
    #print(prt[3121][2])
    return prt2

def index(request):

    if request.method == 'POST':

        uplfile = request.FILES['file']
        print("archivo: " + uplfile.name + "subido correctamente...")
        #precargaarchivo(request)

    else:
        print('No se ha cargado ningun archivo...')

    return render(request, 
        'C:/Users/Leonor Fischer/Documents/re-sys-main/page1/templates/index.html', 
        context={'username': 'Cesar Mendez'})


def precargaarchivo(request):


    uplfile = request.FILES['file'].readlines()

    prt = []
    prt2 = []

    for file in uplfile:
        prt.append('{}'.format(file.strip()))

    for i in prt:
        prt2.append(i.split(','))

    for i in prt2:
        print(i[1])
    #print(prt2[3121][1])

    return render(request,
        'C:/Users/Leonor Fischer/Documents/re-sys-main/page1/templates/precargaarchivo.html',
        context={'data': prt2})










def index2(request):

    docExterno = open("C:/Users/Leonor Fischer/Documents/re-sys-main/page1/templates/index2.html")
    plt = Template(docExterno.read())
    docExterno.close()

    data = pd.read_csv('C:/Users/Leonor Fischer/Documents/re-sys-main/page1/templates/all_seasons.csv', header=0)
    data = data.iloc[:10]
    dataHTML = generate_html(data)
    # write the HTML content to an HTML file
    open("htl.html", "w").write(dataHTML)
    webbrowser.open("htl.html")

    columnas = data.columns
    index = data.index

    #if request.FILES:
     #   uplfile=request.FILES['filecsv']
      #  Context['filename'] = uplfile.name
       # Context['filesize'] = uplfile.size
    
    ctx = Context({
        "username": "Cesar Mendez",
        "columnas": columnas,
        "filas": index,
        "datahtml": dataHTML,
        
	})

    documento = plt.render(ctx)

    return HttpResponse(documento)


def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table")
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # return the html
    return html
