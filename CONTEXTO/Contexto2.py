# INDICADORES RIS3 DE CONTEXTO
# INDICADOR : N de Empresas por cada 100 habitantes
# Nº de empresas
#https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/298?tip=AM&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=393:23092&tv=336:15723&tv=337:15740&tv=3:94
# Nº de habitantes
#https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/9681?tip=AM&tv=356:15668&tv=355:15319&tv=355:15320&tv=355:15321&tv=355:15322&tv=355:15323&tv=355:15324&tv=355:15325&tv=355:15326&tv=355:15327&tv=355:15328&tv=355:15329&tv=355:15330&tv=355:15331&tv=355:15332&tv=355:15333&tv=355:15334&tv=355:15335&tv=355:15336&tv=355:15337&tv=355:15338&tv=355:15339&tv=355:15340&tv=355:15341&tv=355:15342&tv=355:15343&tv=355:15344&tv=355:15345&tv=355:15346&tv=355:15347&tv=355:15348&tv=355:15349&tv=355:15350&tv=355:15351&tv=355:15352&tv=355:15353&tv=355:15354&tv=355:15355&tv=355:15356&tv=355:15357&tv=355:15358&tv=355:15359&tv=355:15360&tv=355:15361&tv=355:15362&tv=355:15363&tv=355:15364&tv=355:15365&tv=355:15366&tv=355:15367&tv=355:15368&tv=355:15369&tv=355:15370&tv=355:15371&tv=355:15372&tv=355:15373&tv=355:15374&tv=355:15375&tv=355:15376&tv=355:15377&tv=355:15378&tv=355:15379&tv=355:15380&tv=355:15381&tv=355:15382&tv=355:15383&tv=355:15384&tv=355:15385&tv=355:15386&tv=355:15387&tv=355:15388&tv=355:15389&tv=355:15390&tv=355:15391&tv=355:15392&tv=355:15393&tv=355:15394&tv=355:15395&tv=355:15396&tv=355:15397&tv=355:15398&tv=355:15399&tv=355:15400&tv=355:15401&tv=355:15402&tv=355:15403&tv=355:15404&tv=355:15405&tv=355:15406&tv=355:15407&tv=355:15408&tv=355:15409&tv=355:15410&tv=355:15411&tv=355:15412&tv=355:15413&tv=355:15414&tv=355:15415&tv=355:15416&tv=355:15417&tv=355:15418&tv=357:15071&tv=349:16473&tv=18:451&tv=260:17338&tv=3:11879

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
def encontrarhab(json, region ,campo , year):
    ind = "-2"
    for i in range(0,len(json)):
        #print("@marcos"+json [i] ["Nombre"].replace(' ', ''))
        #print(region)
        if (json [i] ["Nombre"].replace(' ', '').find((region).replace(' ','')) >= 0):
            #print("ok")
            for j in range (0,len(json [i] ["Data"])):
                if (json[i] ["Data"] [j] ["Anyo"] == year):
                    #print(json[i] ["Data"] [j] ["T3_Periodo"])
                    #print(campo)
                    if(json[i] ["Data"] [j] ["T3_Periodo"].find("enero") >= 0):
                        ind = json[i] ["Data"] [j] ["Valor"]
    return ind

def encontraremp(json,region, year) :
    ind = "-2"
    for i in range(0,len(json)):
        if (json [i] ["Nombre"].replace(' ', '').find((region).replace(' ','')) >= 0):
           for j in range (0,len(json [i] ["Data"])):
                if (json[i] ["Data"] [j] ["Anyo"] == year):
                    if (json[i] ["Data"] [j] ["Anyo"] == year):
                        ind = json[i] ["Data"] [j] ["Valor"]
    return ind
# Simplemente para que no de problemas de ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
with open ('Contexto2.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","Hab","Emp","EmpxHab"])
jsonurl1 ="http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/298?tip=AM&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=393:23092&tv=336:15723&tv=337:15740&tv=3:94"
jsonurl2 ="http://servicios.ine.es/wstempus/js/es/DATOS_TABLA/9681?tip=AM&tv=356:15668&tv=349:16473&tv=70:8997&tv=70:8998&tv=70:8999&tv=70:9000&tv=70:9001&tv=70:9002&tv=70:9003&tv=70:9004&tv=70:9005&tv=70:9006&tv=70:9007&tv=70:9008&tv=70:9009&tv=70:9010&tv=70:9011&tv=70:9012&tv=70:9013&tv=70:9015&tv=70:8995&tv=18:451&tv=260:17338&tv=3:11879"

TotalEmp = requests.get(jsonurl1)
if (str(TotalEmp.status_code) == "200") :
    jsonEmp = TotalEmp.json()
TotalHab = requests.get(jsonurl2)
if (str(TotalHab.status_code) == "200") :
    jsonHab = TotalHab.json()
rango = encontrarrango(jsonEmp)
for j in range(0,len(rango)) :
    yearaux = str(rango[j])
    year = yearaux[0:4]
    fecha = time.strftime("%Y-%m-%d", time.gmtime())
    str1 = ("""1 de enero de""")
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
    with open('Contexto2.csv',mode='a') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        for i in range(0,len(lista)) :
            lista[i].append(encontrarhab(jsonHab, lista [i] [0],str1, rango[j]))
            lista[i].append(encontraremp(jsonEmp,lista[i] [0], rango[j]))
            lista[i].append(str(int(lista[i][5])/float(lista[i][4] / 100)))
            #print(lista[i])
            employee_writer.writerow(lista[i])
            
            
        




