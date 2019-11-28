# INDICADORES RIS 3 CONTEXTO
# Indicador: Tasa de abandono escolar
# Tasa de abandono escolar:
# http://estadisticas.mecd.gob.es/EducaJaxiPx/files/_px/es/xlsx/Formacionyml/EPA2018/Aban/l0/Aban101.px?nocab=1

def  encontrarrango(datframe) :
    # En la fila 6 están los años
    rango = []
    print(datframe)
    b = int(len(datframe.ix[6,:])/3 + 1)
    print(b)
    for i in range (1, b) : #El primer elemento no está relleno
        print(i)
        rango.append(str(datframe.iloc[6,i]))
    return rango

def encontrar(Region, indice, dataframe) :
    ind = "-2"
    b = dataframe.ix[:,0]
    c = b.values.tolist().index(Region)
    ind = dataframe.iloc[c,indice]
    return ind

import pandas as pd
import requests
import wget
import time
import csv
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
link = "http://estadisticas.mecd.gob.es/EducaJaxiPx/files/_px/es/xlsx/Formacionyml/EPA2018/Aban/l0/Aban101.px?nocab=1"
wget.download(link,'/home/pi/Desktop/Contexto')
file = 'Aban101.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('tabla-0')

rango = encontrarrango(df1)
#print(rango)
with open ('Contexto15.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","Abandono"])
indice = 1
for i in range (0, len(rango)) :
    year = rango[i]
    fecha = time.strftime("%Y-%m-%d", time.gmtime())
    Nacional = ['TOTAL',str(year),fecha, 'Nacional' + str(year)]
    Andalucia = ['Andalucía',str(year), fecha, 'Andalucía' + str(year)]
    Aragon = ['Aragón',str(year), fecha, 'Aragón' + str(year)]
    Asturias = ['Asturias, Principado de',str(year), fecha, 'Asturias' + str(year)]
    Baleares = ['Balears, Illes',str(year), fecha, 'Balears' + str(year)]
    Canarias = ['Canarias',str(year), fecha, 'Canarias' + str(year)]
    Cantabria = ['Cantabria (3)',str(year), fecha, 'Cantabria' + str(year)]
    CastillaLeon = ['Castilla y León',str(year), fecha, 'Castilla y León' + str(year)]
    CastillaMancha = ['Castilla-La Mancha',str(year), fecha, 'Castilla - La Mancha' + str(year)]
    Catalunya = ['Cataluña',str(year), fecha, 'Cataluña' + str(year)]
    Valencia = ['Comunitat Valenciana',str(year), fecha, 'Valencia' + str(year)]
    Extremadura = ['Extremadura',str(year), fecha, 'Extremadura' + str(year)]
    Galicia = ['Galicia',str(year), fecha, 'Galicia' + str(year)]
    Madrid = ['Madrid, Comunidad de',str(year), fecha, 'Madrid' + str(year)]
    Murcia = ['Murcia, Región de',str(year), fecha, 'Murcia' + str(year)]
    Navarra = ['Navarra, Comunidad Foral de (3)',str(year), fecha, 'Navarra' + str(year)]
    PaisVasco = ['País Vasco',str(year), fecha, 'País Vasco' + str(year)]
    Rioja = ['Rioja, La (3)',str(year), fecha, 'Rioja' + str(year)]
    Ceuta = ['Ceuta (3)',str(year), fecha, 'Ceuta' + str(year)]
    Melilla = ['Melilla (3)',str(year), fecha, 'Melilla' + str(year)]
    CeutaMelilla = ['CeutaMelilla',str(year), fecha, 'CeutaMelilla' + str(year)]
    lista = [Nacional,Andalucia,Aragon, Asturias, Baleares, Canarias, Cantabria, CastillaLeon, CastillaMancha, Catalunya, Valencia, Extremadura, Galicia, Madrid, Murcia, Navarra, PaisVasco, Rioja, Ceuta, Melilla]
    with open('Contexto15.csv',mode='a') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        for i in range(0,len(lista)) :
            lista[i].append(encontrar(lista [i] [0], indice, df1))
            print(lista[i])
            employee_writer.writerow(lista[i])
    indice = indice + 1
os.remove('Aban101.xlsx')
