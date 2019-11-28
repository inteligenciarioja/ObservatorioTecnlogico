# Proof of Concept - DATOS RRHH

#FUENTE PRINCIPAL: INE JSON API REST E INSTITUTO RIOJANO DE ESTADÍSTICA
# Para ver los indicadores comprobar el excel que hay 37. Ahí están guardadas
# fuentes
# A veces la API Rest devuelve valores null que realmente están informados. Tenerlo en cuenta para el análisis y corrección
# de la base de datos. Por ejemplo Castilla-LaMancha 2011 campos 5 y 6

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
    querystringlimp = "DELETE FROM exampledb.RRHH"
    c = dbconnection.cursor()
    c.execute(querystringlimp)
    dbconnection.commit()
    c.close()
    dbconnection.close()

# CREAR LA TABLA EN LA BASE DE DATOS
#CREATE TABLE RRHH (Region varchar(30), Year varchar(30), LastUpdateDate varchar(30), id varchar(30) primary key, PersEmplIDTotal varchar(30),PersEmplIDTotalMuj varchar(30),PersEmplIDTotalEmp varchar(30),PersEmplIDTotalEmpMuj varchar(30),PersEmplIDTotalAdPub varchar(30),PersEmplIDTotalAdPubMuj varchar(30),PersEmpIDTotalEnsSup varchar(30),PersEmpIDTotalEnsSupMuj varchar(30),InvIDTotal varchar(30),InvIDTotalMuj varchar(30), InvIDTotalEmp varchar(30), InvIDTotalEmpMuj varchar(30),InvIDTotalAdPub varchar(30),InvIDTotalAdPubMuj varchar(30), InvIDTotalEnsSup varchar(30),InvIDTotalEnsSupMuj varchar(30));

def incluirBD(listainc) :
    for i in range (0,len(listainc)) :
        var_string = ', '.join('?' * len(listainc [i]))
        straux = "','".join(listainc [i])
        strauxfinal = "'"+straux+"'"
        querystring = """INSERT INTO exampledb.RRHH (Region,Year,LastUpdateDate,id, PersEmplIDTotal,PersEmplIDTotalMuj,PersEmplIDTotalEmp,PersEmplIDTotalEmpMuj,
                                  PersEmplIDTotalAdPub,PersEmplIDTotalAdPubMuj,PersEmpIDTotalEnsSup,PersEmpIDTotalEnsSupMuj,
                                  InvIDTotal,InvIDTotalMuj, InvIDTotalEmp, InvIDTotalEmpMuj,
                                  InvIDTotalAdPub,InvIDTotalAdPubMuj, InvIDTotalEnsSup,InvIDTotalEnsSupMuj) VALUES (""" + strauxfinal + """);"""
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        print(querystring)
        c = dbconnection.cursor()
        c.execute(querystring)
        dbconnection.commit()
        c.close()
        dbconnection.close()

limpiarBD()
with open ('RRHH.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Region','Year','LastUpdateDate','id', 'PersEmplIDTotal','PersEmplIDTotalMuj','PersEmplIDTotalEmp','PersEmplIDTotalEmpMuj',
                                  'PersEmplIDTotalAdPub','PersEmplIDTotalAdPubMuj','PersEmpIDTotalEnsSup','PersEmpIDTotalEnsSupMuj',
                                  'InvIDTotal','InvIDTotalMuj', 'InvIDTotalEmp', 'InvIDTotalEmpMuj',
                                  'InvIDTotalAdPub','InvIDTotalAdPubMuj', 'InvIDTotalEnsSup','InvIDTotalEnsSupMuj'])

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

    #1) http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07001.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07001.px
    
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07001.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D
            str1 = (lista[i][0] +
                        """, Personal en I+D en EJC: Total personal""")
            #Alguien decidió que era conveniente cambiar los campos de un año para otro
            str1aux = (lista[i][0] +
                        """, Personal en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1, str1aux))
            # Personal total femenino empleado en actividades de I+D
            str2 = (lista[i][0] +
                        """, Personal en I+D en EJC: Mujeres""")
            str2aux = (lista[i][0] +
                        """, Personal en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))
            
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #2) Personal Empleado en Actividades de I+D en el sector empresarial/IPSFL en EJEC
    #http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07002.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07002.px 
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07002.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D. Empresa
            str1 = (lista[i][0] +
                        """, Personal en I+D en EJC: Total personal""")
            str1aux = (lista[i][0] +
                        """, Personal en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,str1aux))
            # Personal total femenino empleado en actividades de I+D. Empresa
            str2 = (lista[i][0] +
                        """, Personal en I+D en EJC: Mujeres""")
            str2aux = (lista[i][0] +
                        """, Personal en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))   
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #3) Personal emplemado en I+D en Administración Pública
    #http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07003.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07003.px
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07003.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D. Adm. Pública
            str1 = (lista[i][0] +
                        """, Personal en I+D en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,str1aux))
            str1aux = (lista[i][0] +
                        """, Personal en EJC: Total personal""")
            # Personal total femenino empleado en actividades de I+D. Adm. Pública
            str2 = (lista[i][0] +
                        """, Personal en I+D en EJC: Mujeres""")
            str2aux = (lista[i][0] +
                        """, Personal en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))   
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #4) Personal Enseñanza superior
    #http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07004.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07004.px
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07004.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D. Adm. Pública
            str1 = (lista[i][0] +
                        """, Personal en I+D en EJC: Total personal""")
            str1aux = (lista[i][0] +
                        """, Personal en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,str1aux))
            # Personal total femenino empleado en actividades de I+D. Adm. Pública
            str2 = (lista[i][0] +
                        """, Personal en I+D en EJC: Mujeres""")
            str2aux = (lista[i][0] +
                        """, Personal en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))   
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    # Seguir mañana por Personal Inverstigador total, que viene de la primera fuente, pero como lo hemos sustuido hay que
    # volver a preguntar
    # 3) Personal Investigador
    #1) http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07001.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07001.px
    
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07001.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D
            str1 = (lista[i][0] +
                        """, Investigadores en EJC: Total personal""")
            str1aux = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,str1aux))
            # Personal total femenino empleado en actividades de I+D
            str2 = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Mujeres""")
            str2aux = (lista[i][0] +
                        """, Investigadores en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))
            
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)  
    # 4) Personal investigador en el sector empresarial
    #http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07002.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07002.px 
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07002.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D. Empresa
            str1 = (lista[i][0] +
                        """, Investigadores en EJC: Total personal""")
            str1aux = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,str1aux))
            # Personal total femenino empleado en actividades de I+D. Empresa
            str2 = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Mujeres""")
            str2aux = (lista[i][0] +
                        """, Investigadores en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))  
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    # 5) Personal investigador en la administración púbica
        #http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07003.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07003.px
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07003.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D. Adm. Pública
            str1 = (lista[i][0] +
                        """, Investigadores en EJC: Total personal""")
            str1aux = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,str1aux))
            # Personal total femenino empleado en actividades de I+D. Adm. Pública
            str2 = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Mujeres""")
            str2aux = (lista[i][0] +
                        """, Investigadores en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))    
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)

    # 6) Personal Investigador en la Enseñanza superior
    #http://www.ine.es/jaxi/Tabla.htm?path=/t14/p057/a2015/l0/&file=07004.px&L=0
    #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2015/l0/07004.px
    IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"""+str(year)+"""/l0/07004.px""")
    if (str(IDTotal.status_code) == "200") :
        IDTotaljson = IDTotal.json()
        for i in range(0,len(lista)) :
            #Personal Total Empleado en actividades de I+D. Adm. Pública
            str1 = (lista[i][0] +
                        """, Investigadores en EJC: Total personal""")
            str1aux = (lista[i][0] +
                        """, Investigadores en I+D en EJC: Total personal""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1,str1aux))
            # Personal total femenino empleado en actividades de I+D. Adm. Pública
            str2 = (lista[i][0] +
                        """, Investigadores en EJC: Total personal""")
            str2aux = (lista[i][0] +
                        """, Investigadores en EJC: Mujeres""")
            lista[i].append(encontrar(IDTotaljson, lista [i] [0], str2,str2aux))  
    else : 
        print(str(year)+"Has no information")
        for i in range(0,len(lista)) :
            lista[i].append(noinfo)
            lista[i].append(noinfo)
    #for i in lista :
    #   print(i)
    # Escribir filas en fichero csv y en la base de datos
    with open ('RRHH.csv',mode='a') as employee_file :
            employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
            for i in range (0,len(lista)) :
                employee_writer.writerow(lista[i])
    incluirBD(lista)
