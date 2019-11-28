# INDICADORES RIS3 CONTEXTO
# Indicador: % de población en I+D sobre población ocupada
# Ocupados
# https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/4940?tip=AM&tv=18:454&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=357:10559&tv=386:21332&tv=3:20258
# Ocupados en I+D
# https://servicios.ine.es/wstempus/js/es/DATOS_TABLA//t14/p057/a2017/l0/02006.px?tip=AM

import requests
import json
import numpy
import time
import csv
import ssl

def unique(lista) :
    listaunica = []
    for x in lista:
        if x not in listaunica :
            listaunica.append(x)
    return listaunica

def encontrarrango(json) :
    lista = []
    for j in range(0,len(json [0] ["Data"])):
        lista.append(json [0] ["Data"] [j] ["Anyo"])
    print(lista)
    return lista
def encontrar(json, region,campo, year) :
    ind = "-2"
    no = {}
    for i in range(0,len(json)):
        if (json [i] ["Nombre"].replace(' ', '').find((region).replace(' ','')) >= 0):
            #print(json [i] ["Nombre"].replace(' ', ''))
            if (json [i] ["Nombre"].replace(' ', '').find((campo).replace(' ','')) >= 0):       
                ind = json[i] ["Data"] [0] ["Valor"]
    if (str(ind).find(".") < 0):
        ind ="-1"
    return ind
def encontrar2(json, region,campo, year) :
    ind = "-2"
    if (region == "Total,") :
        region = "Nacional"
    for i in range(0,len(json)):
        if (json [i] ["Nombre"].replace(' ', '').find((region).replace(' ','')) >= 0):
            for j in range (0,len(json [i] ["Data"])):
                if (json[i] ["Data"] [j] ["Anyo"] == year):
                    ind = json[i] ["Data"] [j] ["Valor"]     
    return ind
    

url11 = "http://servicios.ine.es/wstempus/js/es/DATOS_TABLA//t14/p057/a"
url21 = "/l0/02006.px?tip=AM"
url2 = "http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/4940?tip=AM&tv=18:454&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=357:10559&tv=386:21332&tv=3:20258"

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
with open ('Contexto17.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","Ocupados","PersI+D","Tasa"])

yearnow = time.gmtime(time.time()).tm_year
noinfo = "-1"
fecha = time.strftime("%Y-%m-%d", time.gmtime())
IDTotal2 = requests.get(url2)
if (str(IDTotal2.status_code) == "200") :
    jsonP2 = IDTotal2.json()
    for year in range (2011,yearnow + 1 ) :
        Nacional = ['Total,',str(year),fecha, 'Nacional' + str(year)]
        Andalucia = ['Andalucía',str(year), fecha, 'Andalucía' + str(year)]
        Aragon = ['Aragón',str(year), fecha, 'Aragón' + str(year)]
        Asturias = ['Asturias',str(year), fecha, 'Asturias' + str(year)]
        Baleares = ['Balears',str(year), fecha, 'Balears' + str(year)]
        Canarias = ['Canarias',str(year), fecha, 'Canarias' + str(year)]
        Cantabria = ['Cantabria',str(year), fecha, 'Cantabria' + str(year)]
        CastillaLeon = ['Castilla y León',str(year), fecha, 'Castilla y León' + str(year)]
        CastillaMancha = ['Castilla - La Mancha',str(year), fecha, 'Castilla - La Mancha' + str(year)]
        Catalunya = ['Cataluña',str(year), fecha, 'Cataluña' + str(year)]
        Valencia = ['Comunitat Valenciana',str(year), fecha, 'Valencia' + str(year)]
        Extremadura = ['Extremadura',str(year), fecha, 'Extremadura' + str(year)]
        Galicia = ['Galicia',str(year), fecha, 'Galicia' + str(year)]
        Madrid = ['Madrid',str(year), fecha, 'Madrid' + str(year)]
        Murcia = ['Murcia',str(year), fecha, 'Murcia' + str(year)]
        Navarra = ['Navarra',str(year), fecha, 'Navarra' + str(year)]
        PaisVasco = ['País Vasco',str(year), fecha, 'País Vasco' + str(year)]
        Rioja = ['Rioja',str(year), fecha, 'Rioja' + str(year)]
        Ceuta = ['Ceuta',str(year), fecha, 'Ceuta' + str(year)]
        Melilla = ['Melilla',str(year), fecha, 'Melilla' + str(year)]
        CeutaMelilla = ['CeutaMelilla',str(year), fecha, 'CeutaMelilla' + str(year)]
        lista = [Nacional,Andalucia,Aragon, Asturias, Baleares, Canarias, Cantabria, CastillaLeon, CastillaMancha, Catalunya, Valencia, Extremadura, Galicia, Madrid, Murcia, Navarra, PaisVasco, Rioja, Ceuta, Melilla]
        print(url11+str(year)+url21)
        IDTotal = requests.get(url11+str(year)+url21)
        print(IDTotal.status_code)
        str1 = "Total personal (EJC): Total"
        if (str(IDTotal.status_code) == "200") :
            jsonP = IDTotal.json()
            with open('Contexto17.csv',mode='a') as employee_file :
                employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
                for i in range(0,len(lista)) :
                    lista[i].append(encontrar(jsonP, lista [i] [0],str1, year))
                    lista[i].append(encontrar2(jsonP2, lista [i] [0],str1, year))
                    lista[i].append((float(lista[i][4])/float(lista[i][5]))/1000)
                    print(lista[i])
                    #employee_writer.writerow(lista[i])
