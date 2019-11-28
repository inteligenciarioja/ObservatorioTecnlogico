# INDICADORES RIS3 DE CONTEXTO
# INDICADOR: Tasa de paro mayores de 45 años
# Parados
# http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/4964?tip=AM&tv=18:454&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=360:10573&tv=357:10560&tv=386:21335&tv=3:20258
# Activos
# http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/4932?tip=AM&tv=18:454&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=360:10573&tv=357:10560&tv=386:20278&tv=3:20258


import requests
import json
import numpy
import time
import csv
import ssl
def encontrarrango(json) :
    lista = []
    for j in range(0,len(json [0] ["Data"])):
        lista.append(json [0] ["Data"] [j] ["Anyo"])
    print(lista)
    #print("final rango")
    return lista
def encontrarPar(json, region, campo, year):
    ind = "-2"
    for i in range(0,len(json)):
        if (json [i] ["Nombre"].replace(' ', '').find((region).replace(' ','')) >= 0):
            if ((json [i] ["Nombre"].replace(' ', '').find((campo).replace(' ','')) >= 0)):
                #print (json [i] ["Nombre"].replace(' ', ''))
                #print(region+campo)
                for j in range (0,len(json [i] ["Data"])):
                    if (json[i] ["Data"] [j] ["Anyo"] == year):
                        ind = json[i] ["Data"] [j] ["Valor"]
    return ind
# Simplemente para que no de problemas de ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
with open ('Contexto8.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","Par4554","Par55","Act4554","Act55","TasaParo"])

jsonurl1= "http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/4964?tip=AM&tv=18:454&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=360:10573&tv=357:10560&tv=386:21335&tv=3:20258"
jsonurl2= "http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/4932?tip=AM&tv=18:454&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=360:10573&tv=357:10560&tv=386:20278&tv=3:20258"

TotalPar = requests.get(jsonurl1)
if (str(TotalPar.status_code) == "200") :
    jsonPar = TotalPar.json()
TotalAct = requests.get(jsonurl2)
if (str(TotalAct.status_code) == "200") :
    jsonAct = TotalAct.json()
rango = encontrarrango(jsonPar)
for j in range(0,len(rango)) :
    yearaux = str(rango[j])
    year = yearaux[0:4]
    fecha = time.strftime("%Y-%m-%d", time.gmtime())
    str1 = (""".De 45""")
    str2 = (".55")
    Nacional = ['Nacional',str(year),fecha, 'Nacional' + str(year)]
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
    with open('Contexto8.csv',mode='a') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        for i in range(0,len(lista)) :
            lista[i].append(encontrarPar(jsonPar, lista [i] [0],str1, rango[j]))
            lista[i].append(encontrarPar(jsonPar, lista [i] [0],str2, rango[j]))
            lista[i].append(encontrarPar(jsonAct,lista[i] [0],str1, rango[j]))
            lista[i].append(encontrarPar(jsonAct,lista[i] [0],str2, rango[j]))
            lista[i].append(str(((float(lista[i][4])+float(lista[i][5]))*100)/(float(lista[i][6])+float(lista[i][7]))))
            print(lista[i])
            employee_writer.writerow(lista[i])
