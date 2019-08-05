# Proof of Concetp - DATOS ACTIVIDADES INNOVADORAS

# Fuente: INE JSON API REST
# 1) Gasto Total en Actividades Innovadoras. Miles de Euros
#http://www.ine.es/jaxi/Datos.htm?path=/t14/p061/a2016/l0/&file=03001.px
#http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a2016/l0/03001.px

# 2) Intensidad de Innovacin(Gasto en actividades en % sobre cifra de negocios
# 3) Intensidad de innovación de las empresas con actividad en ID
# 4) Intensidad de innovación de las empresas con actividad innovadora
# 5) % de la cifra de negocios en productos nuevos o mejorados
#http://www.ine.es/jaxi/Tabla.htm?path=/t14/p061/a2016/l0/&file=03002.px&L=0
#http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a2016/l0/03002.px

# 6) % de empresas tecnológicamente innovadoras
# 7) % de empresas con innovaciones no tecnológicas
# 8) % de empresas innovadoras total
# 9) N0 empesas con innovación tecnlógica
# 10) Total de empresas innovadoras
# 11) N empresas con innovaciones no tecnológicas
#http://www.ine.es/jaxi/Datos.htm?path=/t14/p061/a2016/l0/&file=03003.px
#http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a2016/l0/03003.px


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
                if ( json [i] ["Nombre"].replace(' ' , '').find((region + campo).replace(' ', '')) >= 0) :
                    #print(str(json [i]["Data"] [0])) 
                    if((json[i] ["Data"][0]) != excepcion) :
                        valor = (str(json [i]["Data"] [0] ["Valor"]))
                        if (valor.find("None") >= 0) :
                            valor = "-2"
    return valor

def limpiarBD() :
    dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
    querystringlimp = "DELETE FROM exampledb.ActInnovadora"
    c = dbconnection.cursor()
    c.execute(querystringlimp)
    dbconnection.commit()
    c.close()
    dbconnection.close()

# CREAR LA TABLA EN LA BASE DE DATOS
#CREATE TABLE ActInnovadora (Region varchar(30),Year varchar(30),LastUpdateDate varchar(30),id varchar(30) primary key, GastoTotalActInnovadoraMilesEuros varchar(30), Gastoactividadessobrecifranegocio varchar(30),IntInnovacionEmpActID varchar(30), IntInnovacionEmpconActInnovadora varchar(30),Porccifranegociosprodnuevoomejorado varchar(30), Porcemptecinnovadora varchar(30),Porcempnotec varchar(30),Porempinntotal varchar(30),NEmpinntect varchar(30),NEmpeInnovadoras varchar(30),NEmpInnnotec varchar(30));
def incluirBD(listainc) :
    for i in range (0,len(listainc)) :
        var_string = ', '.join('?' * len(listainc [i]))
        straux = "','".join(listainc [i])
        strauxfinal = "'"+straux+"'"
        querystring = """INSERT INTO exampledb.ActInnovadora (Region,Year,LastUpdateDate,id, GastoTotalActInnovadoraMilesEuros, Gastoactividadessobrecifranegocio,IntInnovacionEmpActID, IntInnovacionEmpconActInnovadora,
                                  Porccifranegociosprodnuevoomejorado, Porcemptecinnovadora,Porcempnotec,Porempinntotal,NEmpinntect,NEmpeInnovadoras,NEmpInnnotec ) VALUES (""" + strauxfinal + """);"""
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        print(querystring)
        c = dbconnection.cursor()
        c.execute(querystring)
        dbconnection.commit()
        c.close()
        dbconnection.close()
limpiarBD() 
with open ('ActividadesInnovadoras.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Region','Year','LastUpdateDate','id', 'GastoTotalActInnovadoraMilesEuros', 'Gastoactividadessobrecifranegocio','IntInnovacionEmpActID', 'IntInnovacionEmpconActInnovadora',
                                  'Porccifranegociosprodnuevoomejorado', 'Porcemptecinnovadora','Porcempnotec','Porempinntotal','NEmpinntect','NEmpeInnovadoras','NEmpInnnotec'])
yearnow = time.gmtime(time.time()).tm_year
noinfo = "-1"
fecha = time.strftime("%Y-%m-%d", time.gmtime())
for year in range (2011,yearnow) :
        Nacional = ['Total Nacional',str(year),fecha, 'Nacional' + str(year)]
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
        
        # 1) Gasto Total en Actividades Innovadoras. Miles de Euros
        #http://www.ine.es/jaxi/Datos.htm?path=/t14/p061/a2016/l0/&file=03001.px
        #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a2016/l0/03001.px
        IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a"""+str(year)+"""/l0/03001.px""")
        if (str(IDTotal.status_code) == "200") :
            IDTotaljson = IDTotal.json()
            str1 = (""", Gastos totales en actividades innovadoras en """ + str(year) +
                    """( en miles de euros)""")
            for i in range(0,len(lista)) :
                lista[i].append(encontrar(IDTotaljson, lista [i] [0], str1))
        else : 
            print(str(year)+"Has no information")
            for i in range(0,len(lista)) :
                lista[i].append(noinfo)
        # 2) Intensidad de Innovacin(Gasto en actividades en % sobre cifra de negocios
        # 3) Intensidad de innovación de las empresas con actividad en ID
        # 4) Intensidad de innovación de las empresas con actividad innovadora
        # 5) % de la cifra de negocios en productos nuevos o mejorados
        #http://www.ine.es/jaxi/Tabla.htm?path=/t14/p061/a2016/l0/&file=03002.px&L=0
        #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a2016/l0/03002.px
        #for i in range (0,len(lista)) :
        #    print(lista[i])
        IDTotal = requests.get("""http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a""" + str(year)+"""/l0/03002.px""")
        str1 = ", Intensidad de innovación: Del total de empresas"
        str2 = ", Intensidad de innovación: De las empresas con actividades de I+D"
        str3 = ", Intensidad de innovación: De las empresas con actividades innovadoras"
        str4 = ", % de la cifra de negocios en productos nuevos o mejorados"
        strlista = [str1,str2,str3,str4]

        if (str(IDTotal.status_code) == "200") :
            IDTotaljson = IDTotal.json()
            for j in range (0,len(strlista)) :
                for i in range(0,len(lista)) :
                    lista[i].append(encontrar(IDTotaljson, lista [i] [0], strlista[j]))

        else:
            print(str(year)+"Has no information")
            for j in range (0, len(strlista)) :
                for i in range(0,len(lista)) :
                    lista[i].append(noinfo)

        # 6) % de empresas tecnológicamente innovadoras
        # 7) % de empresas con innovaciones no tecnológicas
        # 8) % de empresas innovadoras total
        # 9) N0 empesas con innovación tecnlógica
        # 10) Total de empresas innovadoras
        # 11) N empresas con innovaciones no tecnológicas
        #http://www.ine.es/jaxi/Datos.htm?path=/t14/p061/a2016/l0/&file=03003.px
        #http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a2016/l0/03003.px
        IDTotal = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p061/a"+str(year)+"/l0/03003.px")
        str1 = ", Empresas con innovaciones tecnológicas, %"
        str2 = ", Empresas con innovaciones no tecnológicas, %"
        str3 = ", Empresas innovadoras, %"
        str4 = ",Empresasconinnovacionestecnológicas,Total"
        str5 = ", Empresas innovadoras, Total"
        str6 = ", Empresas con innovaciones no tecnológicas, Total"
        strlista = [str1,str2,str3,str4, str5, str6]
        if (str(IDTotal.status_code) == "200") :
            IDTotaljson = IDTotal.json()
            for j in range (0,len(strlista)) :
                for i in range(0,len(lista)) :
                    lista[i].append(encontrar(IDTotaljson, lista [i] [0], strlista[j]))

        else:
            print(str(year)+"Has no information")
            for j in range (0, len(strlista)) :
                for i in range(0,len(lista)) :
                    lista[i].append(noinfo)
        #for i in range (0,len(lista)) :
        #       print(lista[i])
        # ESCRIBIR ROWS EN BASE DE DATOS Y EN CSV
        with open ('ActividadesInnovadoras.csv',mode='a') as employee_file :
            employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
            for i in range (0,len(lista)) :
                employee_writer.writerow(lista[i])
        incluirBD(lista)
        
