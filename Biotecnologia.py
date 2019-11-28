# Proof of Concept- Biotecnología
#BIOTECLOGÍA
#GASTO INTERNO EN ACTIVIDADES DE I+D TOTAL DESTINADO A BIOTECNOLOGÍA. MILES DE EUROS
#PERSONAL EN I+D TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
#PERSONAL INVESTIGADOR TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
#https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/bio/a2017/l0/&file=07002.px
#http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/bio/a2017/l0/07002.px

#GASTO INTERNO EN ACTIVIDADES DE I+D EN EL SECTOR EMPRESARIAL DESTINADO A BIOTECNOLOGÍA. MILES DE EUROS
#PERSONAL EN I+D DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA EN EL SECTOR EMPRESARIAL. EJCPERSONA
#INVESTIGADOR DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA EN EL SECTOR EMPRESARIAL. EJC
#https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/bio/a2017/l0/&file=07003.px
#https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/bio/a2017/l0/07003.px

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
def encontrar(json, region, campo, campo2) :
    excepcion = {}
    valor = "-2";
    #print('@marcos')
    #print(campo)
    #print(campo2)
    for i in range (0,len(json)):
                #print('real')
                #print(json [i] ["Nombre"])
                if ( (json [i] ["Nombre"].replace(' ' , '').find((campo).replace(' ', '')) >= 0) or (json [i] ["Nombre"].replace(' ' , '').find((campo2).replace(' ', '')) >= 0)) :
                    #print(str(json [i]["Data"] [0])) 
                    if((json[i] ["Data"][0]) != excepcion) :
                        valor = (str(json [i]["Data"] [0] ["Valor"]))
                        if (valor.find("None") >= 0) :
                            valor = "-2"
    return valor
def limpiarBD() :
    dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
    querystringlimp = "DELETE FROM exampledb.Biotecnologia"
    c = dbconnection.cursor()
    c.execute(querystringlimp)
    dbconnection.commit()
    c.close()
    dbconnection.close()

# CREAR LA TABLA EN LA BASE DE DATOS
#CREATE TABLE Biotecnologia(Region varchar(30), Year varchar(30), LastUpdateDate varchar(30), id varchar(30) primary key, GastoBioTotal varchar(30),
#PersBioTotal varchar(30),InvBioTotal varchar(30),
#GastoBioEmp varchar(30),PersBioEmp varchar(30), InvBioEmp varchar(30));
def incluirBD(listainc) :
    for i in range (0,len(listainc)) :
        var_string = ', '.join('?' * len(listainc [i]))
        straux = "','".join(listainc [i])
        strauxfinal = "'"+straux+"'"
        querystring = """INSERT INTO exampledb.Biotecnologia (Region,Year,LastUpdateDate,id, GastoBioTotal,
                                  PersBioTotal,InvBioTotal,
                                  GastoBioEmp,PersBioEmp, InvBioEmp) VALUES (""" + strauxfinal + """);"""
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        print(querystring)
        c = dbconnection.cursor()
        c.execute(querystring)
        dbconnection.commit()
        c.close()
        dbconnection.close()

limpiarBD()
with open ('Biotecnologia.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Region','Year','LastUpdateDate','id', 'GastoBioTotal',
                                  'PersBioTotal','InvBioTotal',
                                  'GastoBioEmp','PersBioEmp', 'InvBioEmp'])
yearnow = time.gmtime(time.time()).tm_year
noinfo = "-1"
fecha = time.strftime("%Y-%m-%d", time.gmtime())
for year in range (2011,yearnow) :
    Nacional = ['TOTAL',str(year),fecha, 'Nacional' + str(year)]
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

    #GASTO INTERNO EN ACTIVIDADES DE I+D TOTAL DESTINADO A BIOTECNOLOGÍA. MILES DE EUROS
    #PERSONAL EN I+D TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
    #PERSONAL INVESTIGADOR TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
    #https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/bio/a2017/l0/&file=07002.px
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/bio/a2017/l0/07002.px
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/bio/a"""+str(year)+
                           """/l0/07002.px""")
    
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #PERSONAL EN I+D TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
            str1 = (lista[i][0] +
                        """, Gastos internos (miles de euros)""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1, str1))
            #PERSONAL EN I+D TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
            str2 = (lista[i][0] +
                        """, Personal en I+D en EJC: Total personal""")
            str2aux = (lista[i][0] +
                        """, Personal en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2, str2aux))
            #PERSONAL INVESTIGADOR TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
            str3 = (lista[i][0] +
                        """, Investigadores en EJC: Total personal""")
            str3aux = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str3,str3aux))
            
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #GASTO INTERNO EN ACTIVIDADES DE I+D EN EL SECTOR EMPRESARIAL DESTINADO A BIOTECNOLOGÍA. MILES DE EUROS
    #PERSONAL EN I+D DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA EN EL SECTOR EMPRESARIAL. EJCPERSONA
    #INVESTIGADOR DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA EN EL SECTOR EMPRESARIAL. EJC
    #https://www.ine.es/jaxi/Datos.htm?path=/t14/p057/bio/a2017/l0/&file=07003.px
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/bio/a2017/l0/07003.px
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/bio/a"""+str(year)+
                           """/l0/07003.px""")
    
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #PERSONAL EN I+D TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
            str1 = (lista[i][0] +
                        """, Gastos internos (miles de euros)""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1, str1))
            #PERSONAL EN I+D TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
            str2 = (lista[i][0] +
                        """, Personal en I+D en EJC: Total personal""")
            str2aux = (lista[i][0] +
                        """, Personal en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2, str2aux))
            #PERSONAL INVESTIGADOR TOTAL DESTINADO A ACTIVIDADES DE BIOTECNOLOGÍA. EJC
            str3 = (lista[i][0] +
                        """, Investigadores en EJC: Total personal""")
            str3aux = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str3,str3aux))
            
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #for i in lista :
    #   print(i)
    # Introducción en un CSV y en la base de datos
    with open ('RRHH.csv',mode='a') as employee_file :
            employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
            for i in range (0,len(lista)) :
                employee_writer.writerow(lista[i])
    incluirBD(lista)
