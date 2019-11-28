# Proof of Concept - DATOS ALTA TECNOLOGÍA

# Fuente: INE JSON API REST
#1) Gasto en I+D en manufactureras de alta y media-alta tecnología
#2) %GASTO I+D SOBRE EL GASTO EN I+D TOTAL
#3) %gasto I+D SORE EL TOTAL DE GASTO DE SECTOERES DE ALTA TECNOLOGÍA
#4) %gasto I+D SOBRE EL GASTO EN I+D NACIONAL
#5) PERSONAL EN I+D
#6) %PERSONAL I+D SOBRE PERSONAL TOTAL
#7) %NOcupados
#8) %Ocupados sobre el total de ocupados en alta tecnología
#9) %Ocupados sobre el total nacional

#Gasto en I+D en manufactureras de alta y media-alta tecnología
#Gasto en I+D en  de servicios alta tecnología
#Personal en I+D en manufactureras de alta y media-alta tecnología (EJC)
#Personal en I+D de servicios alta tecnología (EJC)

#https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/a2017/l0/&file=01010.px
#http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/01010.px

#GASTO EN I+D TOTAL. Miles de euros (Este es uno de los indicadores y apoyo para calcular también los demás)
#% Gasto total en I+D en sectores alta tecnología sobre el gasto en I+D total
#% Gasto en I+D en manufactureras de alta y media-alta tecnología sobre el gasto en I+D total
#% Personal en I+D en empresas de sectores de alta tecnología sobre total personal I+D
#% Personal en I+D en empresas manufactureras de alta y media-alta tecnología sobre total personal I+D
#% Personal en I+D de servicios alta tecnología sobre total personal I+D

#https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/a2017/l0/&file=02006.px
#https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/02006.px


import requests
import json
import csv
import time
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pprint import pprint
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
def encontrar(json, region, campo) :
    excepcion = {}
    valor = "-2";
    #print('@marcos')
    #print(region + campo)
    for i in range (0,len(json)):
                #print('real')
                #print(json [i] ["Nombre"])
                if ( json [i] ["Nombre"].replace(' ' , '').find((campo).replace(' ', '')) >= 0) :
                    #print(str(json [i]["Data"] [0])) 
                    if((json[i] ["Data"][0]) != excepcion) :
                        valor = (str(json [i]["Data"] [0] ["Valor"]))
                        if (valor.find("None") >= 0) :
                            valor = "-2"
    return valor

def limpiarBD() :
    dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
    querystringlimp = "DELETE FROM exampledb.AltaTecnologia"
    c = dbconnection.cursor()
    c.execute(querystringlimp)
    dbconnection.commit()
    c.close()
    dbconnection.close()

# CREAR LA TABLA EN LA BASE DE DATOS
#CREATE TABLE AltaTecnologia (Region varchar(30), Year varchar(30), LastUpdateDate varchar(30), id varchar(30) primary key, GastoIDManAltayMediaTec varchar(30), GastoIDSerAltTec varchar(30), PersIDManAltayMediaTec varchar(30), PersIDServAltTec varchar(30), GastoIDTotal varchar(30), PersIDTotal varchar(30));  
def incluirBD(listainc) :
    for i in range (0,len(listainc)) :
        var_string = ', '.join('?' * len(listainc [i]))
        straux = "','".join(listainc [i])
        strauxfinal = "'"+straux+"'"
        querystring = """INSERT INTO exampledb.AltaTecnologia (Region,Year,LastUpdateDate,id, GastoIDManAltayMediaTec, GastoIDSerAltTec,
                                  PersIDManAltayMediaTec,PersIDServAltTec,GastoIDTotal,PersIDTotal) VALUES (""" + strauxfinal + """);"""
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        print(querystring)
        c = dbconnection.cursor()
        c.execute(querystring)
        dbconnection.commit()
        c.close()
        dbconnection.close()

limpiarBD() 
with open ('AltaTecnologia.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Region','Year','LastUpdateDate','id', 'GastoIDManAltayMediaTec', 'GastoIDSerAltTec',
                                  'PersIDManAltayMediaTec','PersIDServAltTec','GastoIDTotal','PersIDTotal'])

yearnow = time.gmtime(time.time()).tm_year
noinfo = "-1"
fecha = time.strftime("%Y-%m-%d", time.gmtime())
for year in range (2011,yearnow) :
    Nacional = ['Total',str(year),fecha, 'Nacional' + str(year)]
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

        
        # 1  )
        #Gasto en I+D en manufactureras de alta y media-alta tecnología
        #Gasto en I+D en  de servicios alta tecnología
        #Personal en I+D en manufactureras de alta y media-alta tecnología (EJC)
        #Personal en I+D de servicios alta tecnología (EJC)
        #https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/a2017/l0/&file=01010.px
        #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/01010.px

    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/01010.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Gasto en I+D en manufactureras de alta y media-alta tecnología
            str1 = ("""manufactureras de alta y media-alta tecnología, """ + lista[i][0] +
                        """, Gastos en I+D (miles de euros)""")
            #Gasto en I+D en  de servicios alta tecnología
            str2 = ("""de servicios alta tecnología, """ + lista[i][0] +
                        """, Gastos en I+D (miles de euros)""")
            #Personal en I+D en manufactureras de alta y media-alta tecnología (EJC)
            str3 = ("""manufactureras de alta y media-alta tecnología,"""+ lista[i][0]
                    + """, Personal en EJC""")
            #Personal en I+D de servicios alta tecnología (EJC)
            str4 = ("""de servicios alta tecnología,"""+ lista[i][0]
                    + """, Personal en EJC""")
    
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1))
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2))
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str3))
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str4))
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #2) 
    #GASTO EN I+D TOTAL. Miles de euros (Este es uno de los indicadores y apoyo para calcular también los demás)
    #% Gasto total en I+D en sectores alta tecnología sobre el gasto en I+D total
    #% Gasto en I+D en manufactureras de alta y media-alta tecnología sobre el gasto en I+D total
    #% Personal en I+D en empresas de sectores de alta tecnología sobre total personal I+D
    #% Personal en I+D en empresas manufactureras de alta y media-alta tecnología sobre total personal I+D
    #% Personal en I+D de servicios alta tecnología sobre total personal I+D

    #https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/a2017/l0/&file=02006.px
    #https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/02006.px
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+
                           """/l0/02006.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            str1 = (lista[i][0] + """, Gastos internos (miles de euros): Total""")#Total, Gastos internos (miles de euros): Total
            str2 = (lista[i][0] +""", Personal en equivalencia a jornada completa: Total personal (EJC): Total""") # , Personal en equivalencia a jornada completa: Total personal (EJC): Total
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1))
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2))
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #En principio con toda esta info extraida tengo todos los indicadores cubiertos, falta calcularlos, podría ser
    # conveniente hacerlo mediante pandas para hacer cálculos rápidos. Lo haré finalmente en la parte de representación
    # porque el resto puede ser controlado mediante excel y así no complico la tabla

    # INCLUIR EN EL CSV
    with open ('AltaTecnologia.csv',mode='a') as employee_file :
            employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
            for i in range (0,len(lista)) :
                employee_writer.writerow(lista[i])

    # INCLUIR EN LA BASE DE DATOS
    incluirBD(lista)
    #for i in range(0,len(lista)) :
        #print(lista[i])

    
