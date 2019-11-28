# INDICADORES RIS3 CONTEXTO
# %HOGARES CON BANDA ANCHA
# http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/t25/p450/base_2011/a2019/l0/05001.px?tip=AM
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
    for i in range(0,len(json)):
        if (json [i] ["Nombre"].replace(' ', '').find((region).replace(' ','')) >= 0):
            if (json [i] ["Nombre"].replace(' ', '').find((campo).replace(' ','')) >= 0):       
                ind = json[i] ["Data"] [0] ["Valor"]     
    return ind
url1 = "http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/t25/p450/base_2011/a"
url2 = "/l0/05001.px?tip=AM"
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
with open ('Contexto18.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","ind"])

yearnow = time.gmtime(time.time()).tm_year
noinfo = "-1"
fecha = time.strftime("%Y-%m-%d", time.gmtime())
for year in range (2011,yearnow + 1 ) :
    Nacional = ['nacional',str(year),fecha, 'Nacional' + str(year)]
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
    print(url1+str(year)+url2)
    IDTotal = requests.get(url1+str(year)+url2)
    print(IDTotal.status_code)
    str1 = "Viviendas con conexión de Banda Ancha (ADSL, Red de cable, etc.)"
    if (str(IDTotal.status_code) == "200") :
        jsonP = IDTotal.json()
        with open('Contexto18.csv',mode='a') as employee_file :
            employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
            for i in range(0,len(lista)) :
                lista[i].append(encontrar(jsonP, lista [i] [0],str1, year))
                print(lista[i])
                employee_writer.writerow(lista[i])
         
