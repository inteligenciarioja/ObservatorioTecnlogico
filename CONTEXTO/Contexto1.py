# INDICADORES RIS3 DE CONTEXTO
# INDICADOR 1: Tasa de Variación Interanual del PIB
# FUENTE: INE JSON API REST
# 1) Tasa de variación del PIB
# http://www.ine.es/jaxi/Tabla.html?path=/t35/p010/base2010/l0/%file=01002.px&L=0
# http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t35/p010/base2010/l0/01002.px

import requests
import json
import numpy
import time
import csv
#from codaio import Coda
import ssl

def encontrarrango(json) :
    lista = []
    for j in range(0,len(json [0] ["Data"])):
        lista.append(json [0] ["Data"] [j] ["NombrePeriodo"])
    #print(lista)
    #print("final rango")
    return lista
def encontrar(json, region, campo,year) :
    #print(year)
    ind = "-2"
    for i in range(0, len(json)) :
        if (json [i] ["Nombre"].replace(' ', '').find((region+campo).replace(' ','')) >= 0):
            #print(json [i] ["Nombre"])
            for j in range (0,len(json [i] ["Data"])):
                if (json[i] ["Data"] [j] ["NombrePeriodo"] == year):
                    #print(json[i] ["Data"] [j] ["NombrePeriodo"])
                    #print(json[i] ["Data"] [j] ["Valor"])
                    ind = json[i] ["Data"] [j] ["Valor"]
    return ind


year = 2019
jsonurl = "http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t35/p010/base2010/l0/01002.px"

API_KEY = 'c5d228f1-a38e-4956-b6e6-f6ceaac089d0'
docid="G6ody-h41g"
tabid = "grid-r2hvl_u-eJ"
columnid = "c-JLQHCLTG3gri"
columnregion = "c-dvIIwWnDeP"
columnyear = "c-0brmLRAw0y"
columnind = "c-X2A3yhibUX"
# Simplemente para que no de problemas de ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
    
#coda = Coda(API_KEY)
# 1) Tasa de Variación Interanual
# En este caso el json contiene toda la serie
with open ('Contexto1.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","ind"])
IDTotal = requests.get(jsonurl)
if (str(IDTotal.status_code) == "200") :
            IDTotaljson = IDTotal.json()
            rango = encontrarrango(IDTotaljson)
            for j in range (0, len(rango)-1) :
                yearaux = rango[j]
                year = yearaux[0:4]
                fecha = time.strftime("%Y-%m-%d", time.gmtime())
                str1 = (""", PRODUCTO INTERIOR BRUTO A PRECIOS DE MERCADO, Tasas de variación interanuales""")
                Nacional = ['TOTAL NACIONAL',str(year),fecha, 'Nacional' + str(year)]
                Andalucia = ['Andalucía',str(year), fecha, 'Andalucía' + str(year)]
                Aragon = ['Aragón',str(year), fecha, 'Aragón' + str(year)]
                Asturias = ['Asturias, Principado de',str(year), fecha, 'Asturias' + str(year)]
                Baleares = ['Balears, Illes',str(year), fecha, 'Balears' + str(year)]
                Canarias = ['Canarias',str(year), fecha, 'Canarias' + str(year)]
                Cantabria = ['Cantabria',str(year), fecha, 'Cantabria' + str(year)]
                CastillaLeon = ['Castilla y León',str(year), fecha, 'Castilla y León' + str(year)]
                CastillaMancha = ['Castilla - La Mancha',str(year), fecha, 'Castilla - La Mancha' + str(year)]
                Catalunya = ['Cataluña',str(year), fecha, 'Cataluña' + str(year)]
                Valencia = ['Comunitat Valenciana',str(year), fecha, 'Valencia' + str(year)]
                Extremadura = ['Extremadura',str(year), fecha, 'Extremadura' + str(year)]
                Galicia = ['Galicia',str(year), fecha, 'Galicia' + str(year)]
                Madrid = ['Madrid, Comunidad de',str(year), fecha, 'Madrid' + str(year)]
                Murcia = ['Murcia, Región de',str(year), fecha, 'Murcia' + str(year)]
                Navarra = ['Navarra, Comunidad Foral de',str(year), fecha, 'Navarra' + str(year)]
                PaisVasco = ['País Vasco',str(year), fecha, 'País Vasco' + str(year)]
                Rioja = ['Rioja, La',str(year), fecha, 'Rioja' + str(year)]
                Ceuta = ['Ceuta',str(year), fecha, 'Ceuta' + str(year)]
                Melilla = ['Melilla',str(year), fecha, 'Melilla' + str(year)]
                CeutaMelilla = ['CeutaMelilla',str(year), fecha, 'CeutaMelilla' + str(year)]
                lista = [Nacional,Andalucia,Aragon, Asturias, Baleares, Canarias, Cantabria, CastillaLeon, CastillaMancha, Catalunya, Valencia, Extremadura, Galicia, Madrid, Murcia, Navarra, PaisVasco, Rioja, Ceuta, Melilla]
                with open ('Contexto1.csv',mode='a') as employee_file :
                    employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
                    for i in range(0,len(lista)) :
                        lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,rango[j]))
                        payload = {
                        'rows': [
                        {   
                    'cells': [
                        {'column': columnid, 'value': lista[i][3]},
                        {'column': columnregion, 'value':lista[i][0]},
                        {'column': columnyear, 'value':lista[i][1]},
                        {'column': columnind, 'value':lista[i][4]}
                        ],
                        },
                        ],
                    "keyColumns" : [
                        columnid
                        ]
                        }
                        employee_writer.writerow(lista[i])
                        #coda.upsert_row(docid,tabid,payload)
