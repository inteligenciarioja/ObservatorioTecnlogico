# Prueba de concepto

# Example for DATOS INE I+D
# Python scritp for asking INE API for Cifra de negocios del total de empresas (Incluye los Sectores manufactureros de alta y media-alta tecnología y los servicios de alta tecnología)
# https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/DCC50?nult=10

import requests
import json
import csv
import time
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
#Creación de la tabla en la base de datos
#CREATE TABLE IDAnalisis (Region varchar(30), Year varchar(10) , LastUpdateDate varchar(20), id varchar(30) primary key,GastoIDTotalMilesEuros varchar(20), GastoIDTotalPorc varchar(20),GastoIDADPubMilesEuros varchar(20), GastoIDAPubPorc varchar(20),GastoIDEnsSupMilesEuros varchar(20), GastoIDEnsSupPorc varchar(20),GastoIDEmpmilesEuros varchar(20),GastoIDEmpPorc varchar(20),GastoIDIPSFLMilesEuros varchar(20),GastoIDIPSFLPorc varchar(20), PorcaPIB varchar(20));

# Example of use
#c = db_connection.cursor()
#c.execute("INSERT INTO exampledb.example (id, name, job) VALUES (null, 'Marcos', 'Ingeniero')")
#c.execute("SELECT * FROM exampledb.example")
#print (c.fetchall)

#for row in c.fetchall() :
#    print(row)




def encontrar(json, region, campo) :
    valor = "-2";
    for i in range (0,len(json)):
                if ( json [i] ["Nombre"].find(region + campo) >= 0) :
                    valor = (str(json [i]["Data"] [0] ["Valor"]))
                    if (valor.find("None") >= 0) :
                        valor = "-2"
    return valor
def encontrarIDPIBMer (json, region, yearfunc) :
    valor = "-2"
    for i in range (0, len(json)) :
        if ( json [i] ["Nombre"].find(region) >= 0) :
           for j in range (0,len(json [i] ["Data"])) :
               if (json [i] ["Data"] [j] ["NombrePeriodo"].find(yearfunc) >= 0) :
                   valor = (str(json [i] ["Data"] [j] ["Valor"]))
                   if (valor.find("None") >= 0) :
                       valor = "-3"
    return valor
def actlista (jsonact, yearfuncact, listareg) :
    for i in range (0, len(listareg)) :
        listareg[i].append(encontrarIDPIBMer (jsonact, listareg [i][0], str(yearfuncact)))
    return listareg
def incluirBD(listainc) :
    for i in range (0,len(listainc)) :
        var_string = ', '.join('?' * len(listainc [i]))
        straux = "','".join(listainc [i])
        strauxfinal = "'"+straux+"'"
        querystring = """INSERT INTO exampledb.IDAnalisis (Region, Year, LastUpdateDate, id ,GastoIDTotalMilesEuros , GastoIDTotalPorc ,GastoIDADPubMilesEuros ,
        GastoIDAPubPorc ,GastoIDEnsSupMilesEuros , GastoIDEnsSupPorc ,GastoIDEmpmilesEuros ,GastoIDEmpPorc ,
        GastoIDIPSFLMilesEuros ,GastoIDIPSFLPorc , PorcaPIB ) VALUES (""" + strauxfinal + """);"""
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        #print(querystring)
        c = dbconnection.cursor()
        c.execute(querystring)
        dbconnection.commit()
        c.close()
        dbconnection.close()

def limpiarBD() :
    dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
    querystringlimp = "DELETE FROM exampledb.IDAnalisis"
    c = dbconnection.cursor()
    c.execute(querystringlimp)
    dbconnection.commit()
    c.close()
    dbconnection.close()
    
# Send GET to final Destination
#r = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/DCC50?nult=10")
# Obtain JSON
#r.json()
# pprint(r.json())

# Parse Json
#y = json.loads(r.text)
#print(y["Nombre"])
#print(y["Data"])
#print("--------------------------")
#print(y["Data"][1])
#print("++++++++++++++++++++++++++");
#print(y["Data"][1]["Valor"])
#print("++++++++++++++++++++++++++");
#print(len(y["Data"]))

# Phase 1) Obtain Information from each year
with open ('I+DGastos.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Region','Year','LastUpdateDate','id','GASTO EN I+D TOTAL. Miles de Euros','GASTO EN I+D TOTAL EN % SOBRE TOTAL NACIONAL','GASTO EN I+D SECTOR ADMINISTRACIÓN PÚBLICA. Miles de euros',
                              '% DE GASTO I+D ADMINISTRACIÓN PÚBLICA SOBRE EL TOTAL NACIONAL', 'GASTO EN I+D ENSEÑANZA SUPERIOR.Miles de Euros',
                              '%Gasto I+D Enseñanza superior sobre el nacional','GASTO EN I+D SECTOR EMPRESAS. Miles de euros',
                              '% DE GASTO I+D EMPRESAS SOBRE EL TOTAL NACIONAL',
                          'GASTO EN I+D SECTOR IPSFL','% DE GASTO I+D  IPSFL SOBRE EL TOTAL NACIONAL','Porcentaje de gastos en I+D respecto al PIB a precios de mercado por comunidades autónomas. Serie 2003-2016'])
noinfo = "-1"
yearnow = time.gmtime(time.time()).tm_year
#print("yearnow ="  + str(yearnow))
# Porcentaje de gastos en I+D respecto al PIB a precios de mercado por comunidades autónomas. Serie 2003-2016
statuscode = "404"
yearquery = yearnow
limpiarBD()

while (statuscode !=  "200" ) :
        IDPorcPIB = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(yearquery)+"/l0/02007.px")
        if (str(IDPorcPIB.status_code) == "200") :
            #print(str(yearquery)+"Ha dado 200")
            IDPorcPIBjson = IDPorcPIB.json()
            statuscode = "200"
        else :
            #print(str(yearquery)+"Has no information query")
            yearquery = yearquery - 1
            #print(str(yearquery))
        #print(str(yearquery) + "Yearquerye")
        #print(statuscode)
fecha = time.strftime("%Y-%m-%d", time.gmtime())
# GASTO EN I+D TOTAL. Miles de Euros y % GASTO EN I+D TOTAL EN % SOBRE TOTAL NACIONA
for year in range (2010,yearnow) :
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
        Valencia = ['Valencia',str(year), fecha, 'Valencia' + str(year)]
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
        #print("2222" + lista [0] [1] )
        IDTotal = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/02006.px")
        if (str(IDTotal.status_code) == "200") :
            IDTotaljson = IDTotal.json()
            GastosIntTot = ", Gastos internos (miles de euros): Total"
            GastoIntPor = ", Gastos internos (miles de euros): %"
            Nacional.append(encontrar(IDTotaljson,"Total",GastosIntTot))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastosIntTot))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastosIntTot))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastosIntTot))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastosIntTot))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastosIntTot))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastosIntTot))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastosIntTot))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastosIntTot))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastosIntTot))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastosIntTot))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastosIntTot))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastosIntTot))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastosIntTot))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastosIntTot))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastosIntTot))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastosIntTot))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastosIntTot))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastosIntTot))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastosIntTot))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastosIntTot))

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))
    
        else :
            print(str(year)+"Has no information")
            
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
            

# GASTO EN I+D SECTOR ADMINISTRACIÓN PÚBLICA. Miles de euros y % DE GASTO I+D ADMINISTRACIÓN # PÚBLICA SOBRE EL TOTAL NACIONAL
        IDAdPub = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07003.px")
        if (str(IDAdPub.status_code) == "200") :
            IDAdPubjson = IDAdPub.json()
            IDTotaljson = IDAdPubjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
    


# GASTO EN I+D ENSEÑANZA SUPERIOR.Miles de Euros y %Gasto I+D Enseñanza superior sobre el nacional
        IDEnSup = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07004.px")
        if (str(IDEnSup.status_code) == "200") :
            IDEnSupjson = IDEnSup.json()
            IDTotaljson = IDEnSupjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)

# GASTO EN I+D SECTOR EMPRESAS. Miles de euros y % DE GASTO I+D EMPRESAS SOBRE EL TOTAL #NACIONAL
        IDemp = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07002.px")
        if (str(IDemp.status_code) == "200") :
            IDempjson = IDemp.json()
            IDTotaljson = IDempjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears, Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)

# GASTO EN I+D SECTOR IPSFL Y % DE GASTO I+D  IPSFL SOBRE EL TOTAL NACIONAL
        IDIPSFL = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07002a.px")
        if (str(IDIPSFL.status_code) == "200") :
            IDIPSFLjson = IDIPSFL.json()
            IDTotaljson = IDIPSFLjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears,Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias, Principado de",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Balears,Illes",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunitat Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid, Comunidad de",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia, Región de",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra, Comunidad Foral de",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja, La",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
            Nacional.append(noinfo)
            Andalucia.append(noinfo)
            Aragon.append(noinfo)
            Asturias.append(noinfo)
            Baleares.append(noinfo)
            Canarias.append(noinfo)
            Cantabria.append(noinfo)
            CastillaLeon.append(noinfo)
            CastillaMancha.append(noinfo)
            Catalunya.append(noinfo)
            Valencia.append(noinfo)
            Extremadura.append(noinfo)
            Galicia.append(noinfo)
            Madrid.append(noinfo)
            Murcia.append(noinfo)
            Navarra.append(noinfo)
            PaisVasco.append(noinfo)
            Rioja.append(noinfo)
            CeutaMelilla.append(noinfo)
            Ceuta.append(noinfo)
            Melilla.append(noinfo)
            
# GASTO ID SOBRE PIB VALOR DE MERCADO
        IDTotaljson = IDPorcPIBjson
        actlista (IDTotaljson, year, lista)
        #Andalucia.append(encontrarIDPIBMer (IDTotaljson, "Andalucía", str(year)))
        #print ("Prueba funcin id sobre pib mercado - Año"+str(year) +" valor" + res)
# ------------------------------------------------------------------------------------------------------------------
        # Phase 2) Connect & Insert information in a csv
        with open ('I+DGastos.csv',mode='a') as employee_file :
            employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
            #print("Row obtenida al final"+str(year))
            #print(Andalucia)
            #print(Nacional)
            employee_writer.writerow(Nacional)
            employee_writer.writerow(Andalucia)
            employee_writer.writerow(Aragon)
            employee_writer.writerow(Asturias)
            employee_writer.writerow(Baleares)
            employee_writer.writerow(Canarias)
            employee_writer.writerow(Cantabria)
            employee_writer.writerow(CastillaLeon)
            employee_writer.writerow(CastillaMancha)
            employee_writer.writerow(Catalunya)
            employee_writer.writerow(Valencia)
            employee_writer.writerow(Extremadura)
            employee_writer.writerow(Galicia)
            employee_writer.writerow(Madrid)
            employee_writer.writerow(Murcia)
            employee_writer.writerow(Navarra)
            employee_writer.writerow(PaisVasco)
            employee_writer.writerow(Rioja)
            #employee_writer.writerow(CeutaMelilla)
            employee_writer.writerow(Ceuta)
            employee_writer.writerow(Melilla)
            #print(', '.join(Nacional))

            
# ---------------------------------------------------------------------------------------------------------------------------
#       Phase3) Transfer csv to Database
# Hay que definir una funcion que recorra toda la lista y que vaya uno por uno
# generando el string y haciendo la insercion. Como no necesitaremos hacer cargas
# acumulativas - upserts - borraremos la tabla en cada momento que se ejecute
# EXAMPLE
        #var_string = ', '.join('?' * len(Nacional))
        #straux = "','".join(Nacional)
        #strauxfinal = "'"+straux+"'"
        #querystring = """INSERT INTO exampledb.IDAnalisis (Region, Year, LastUpdateDate, id ,GastoIDTotalMilesEuros , GastoIDTotalPorc ,GastoIDADPubMilesEuros ,
        #GastoIDAPubPorc ,GastoIDEnsSupMilesEuros , GastoIDEnsSupPorc ,GastoIDEmpmilesEuros ,GastoIDEmpPorc ,
        #GastoIDIPSFLMilesEuros ,GastoIDIPSFLPorc , PorcaPIB ) VALUES (""" + strauxfinal + """);"""
        #print(querystring)

        #dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
        #                       user='exampleuser', passwd='pimylifeup')

        #c = dbconnection.cursor()
        #c.execute(querystring)
        #dbconnection.commit()
        #c.close()

        incluirBD(lista) 


#       Phase 4) Retrieving data to be plotted
# Plotearemos el gatos interno de la rioja de 2010 hasta ahora

# GASTO I+D LA RIOJA
querycount = """SELECT count(id) FROM exampledb.IDAnalisis WHERE Region = 'Rioja'"""
querystring = """SELECT id, Year, GastoIDTotalMilesEuros FROM exampledb.IDAnalisis WHERE Region = 'Rioja'"""
#print(querystring)
dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
c = dbconnection.cursor()
c.execute(querystring)
result = c.fetchall()
#print(result [0] [0])
axisx = []
axisy = []
for row in result :
    if (row[2] != '-1') :
        axisx.append(int(row[1]))
        axisy.append(float(row[2]))
c.close()
dbconnection.close()
print(axisx)
print(axisy)



# EVOLUCIÓN DEL GASTO INTERNO SOBRE EL PIB EN %
yearint = 2017

#querystring = """SELECT id, Year, PorcaPIB FROM exampledb.IDAnalisis WHERE Year = '""" + str(yearint) + """' OR Year = '"""+str(yearnow-1)+"""'"""
querystring = """SELECT id, Region, Year, PorcaPIB FROM exampledb.IDAnalisis WHERE Year = '""" + str(yearint) + """'"""
dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
c = dbconnection.cursor()
c.execute(querystring)
result = c.fetchall()
Group = []
values = []
for row in result :
    #print(row)
    Group.append(str(row [1]))
    values.append(float(row [3]))

querystring = """SELECT id, Region, Year, PorcaPIB FROM exampledb.IDAnalisis WHERE Year = '""" + str(yearint-1) + """'"""
c.execute(querystring)
result= c.fetchall()
Groupant = []
valuesant = []
for row in result :
    #print(row)
    Groupant.append(str(row [1]))
    valuesant.append(float(row [3]))
plt.figure()
#plt.subplot('121')
plt.title('Gasto I+D Rioja. Miles de Euros')
plt.plot(axisx,axisy,'go')
plt.plot(axisx,axisy,'k')
#plt.subplot('122')
plt.figure()
barwith = 0.25
x = np.arange(len(Group))
x2 = [b + barwith for b in x]
plt.bar(x,values, width = barwith, label = '2017')
plt.bar(x2,valuesant, width = barwith, label = '2016')
plt.xticks(x,Group)
plt.legend()
plt.show()
c.close()
dbconnection.close()
