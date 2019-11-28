# INDICADORES RIS 3 CONTEXTO
# Indicador: PIB per Capita
# Pib Per Capita:
# https://www.ine.es/daco/daco42/cre00/b2010/pr_cre.xlsx

import pandas as pd
import requests
import wget
import time
import csv
import os

def encontrarrango() :
    year = 2001
    rango = []
    file = 'pr_cre.xlsx'
    xl = pd.ExcelFile(file)
    df1 = xl.parse('Tabla_2')
    b = df1.loc[df1['Contabilidad Regional de España - Base 2010'] == "ANDALUCÍA"]
    rangoindice = int(((b.size - 7)/4) + 1)
    for i in range (0,rangoindice) :
        rango.append(year)
        year = year+1
    return rango
def encontrar(Region, indice, dataframe) :
    if (Region.find("Nacional") >= 0):
        Region = "Total Nacional"
    else :
        Region = Region.upper()
    ind = "-2"
    #print(Region.upper())
    b = dataframe.loc[dataframe['Contabilidad Regional de España - Base 2010'] == Region]
    #print(indice)
    ind = b.iloc[0][indice]
    return ind

# Nos bajamos el fichero
link = "https://www.ine.es/daco/daco42/cre00/b2010/pr_cre.xlsx"
wget.download(link,'/home/pi/Desktop/Contexto')
file = 'pr_cre.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Tabla_2')
# Preparamos el fichero de salida
with open ('Contexto3.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","PIBperCapita"])

#La tabla comienza precisamente este año
rango = encontrarrango()
print(rango)
indice = int(6)
for i in range (0, len(rango)) :
    year = rango[i]
    indice = int(6 + i*4)
    fecha = time.strftime("%Y-%m-%d", time.gmtime())
    Nacional = ['Nacional',str(year),fecha, 'Nacional' + str(year)]
    Andalucia = ['Andalucía',str(year), fecha, 'Andalucía' + str(year)]
    Aragon = ['Aragón',str(year), fecha, 'Aragón' + str(year)]
    Asturias = ['Asturias, principado de',str(year), fecha, 'Asturias' + str(year)]
    Baleares = ['Balears, illes',str(year), fecha, 'Balears' + str(year)]
    Canarias = ['Canarias',str(year), fecha, 'Canarias' + str(year)]
    Cantabria = ['Cantabria',str(year), fecha, 'Cantabria' + str(year)]
    CastillaLeon = ['Castilla y León',str(year), fecha, 'Castilla y León' + str(year)]
    CastillaMancha = ['Castilla - La Mancha',str(year), fecha, 'Castilla - La Mancha' + str(year)]
    Catalunya = ['Cataluña',str(year), fecha, 'Cataluña' + str(year)]
    Valencia = ['Comunitat Valenciana',str(year), fecha, 'Valencia' + str(year)]
    Extremadura = ['Extremadura',str(year), fecha, 'Extremadura' + str(year)]
    Galicia = ['Galicia',str(year), fecha, 'Galicia' + str(year)]
    Madrid = ['Madrid, comunidad de',str(year), fecha, 'Madrid' + str(year)]
    Murcia = ['Murcia, región de',str(year), fecha, 'Murcia' + str(year)]
    Navarra = ['Navarra, comunidad foral de',str(year), fecha, 'Navarra' + str(year)]
    PaisVasco = ['País Vasco',str(year), fecha, 'País Vasco' + str(year)]
    Rioja = ['Rioja, La',str(year), fecha, 'Rioja' + str(year)]
    Ceuta = ['Ceuta',str(year), fecha, 'Ceuta' + str(year)]
    Melilla = ['Melilla',str(year), fecha, 'Melilla' + str(year)]
    CeutaMelilla = ['CeutaMelilla',str(year), fecha, 'CeutaMelilla' + str(year)]
    lista = [Nacional,Andalucia,Aragon, Asturias, Baleares, Canarias, Cantabria, CastillaLeon, CastillaMancha, Catalunya, Valencia, Extremadura, Galicia, Madrid, Murcia, Navarra, PaisVasco, Rioja, Ceuta, Melilla]
    with open('Contexto3.csv',mode='a') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        for i in range(0,len(lista)) :
            lista[i].append(encontrar(lista [i] [0], indice, df1))
            print(lista[i])
            employee_writer.writerow(lista[i])

os.remove("pr_cre.xlsx")
