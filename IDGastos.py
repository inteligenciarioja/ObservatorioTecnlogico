# Prueba de concepto

# Example for DATOS INE I+D
# Python scritp for asking INE API for Cifra de negocios del total de empresas (Incluye los Sectores manufactureros de alta y media-alta tecnología y los servicios de alta tecnología)
# https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/DCC50?nult=10

import requests
import json
import csv
from pprint import pprint

def encontrar(json, region, campo) :
    valor = "";
    for i in range (0,len(json)):
                if ( IDTotaljson [i] ["Nombre"].find(region + campo) >= 0) :
                    valor = (str(json [i]["Data"] [0] ["Valor"]))
    return valor

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
        employee_writer.writerow(['Rfegion','Year','GASTO EN I+D TOTAL. Miles de Euros','GASTO EN I+D TOTAL EN % SOBRE TOTAL NACIONAL','GASTO EN I+D SECTOR ADMINISTRACIÓN PÚBLICA. Miles de euros',
                              '% DE GASTO I+D ADMINISTRACIÓN PÚBLICA SOBRE EL TOTAL NACIONAL', 'GASTO EN I+D ENSEÑANZA SUPERIOR.Miles de Euros',
                              '%Gasto I+D Enseñanza superior sobre el nacional','GASTO EN I+D SECTOR EMPRESAS. Miles de euros',
                              '% DE GASTO I+D EMPRESAS SOBRE EL TOTAL NACIONAL','% DE GASTO I+D EMPRESAS SOBRE EL TOTAL #NACIONAL',
                              'GASTO EN I+D SECTOR IPSFL','% DE GASTO I+D  IPSFL SOBRE EL TOTAL NACIONAL'])#,'Porcentaje de gastos en I+D respecto al PIB a precios de mercado por comunidades autónomas. Serie 2003-2016'])
# GASTO EN I+D TOTAL. Miles de Euros y % GASTO EN I+D TOTAL EN % SOBRE TOTAL NACIONA
for year in range (2000,2019) :
        Nacional = ['Nacional',str(year)]
        Andalucia = ['Andalucia',str(year)]
        Aragon = ['Aragon',str(year)]
        Asturias = ['Asturias',str(year)]
        Baleares = ['Baleares',str(year)]
        Canarias = ['Canarias',str(year)]
        Cantabria = ['Cantabria',str(year)]
        CastillaLeon = ['CastillaLeon',str(year)]
        CastillaMancha = ['CastillaMancha',str(year)]
        Catalunya = ['Cataluña',str(year)]
        Valencia = ['Valencia',str(year)]
        Extremadura = ['Extremaura',str(year)]
        Galicia = ['Galicia',str(year)]
        Madrid = ['Madrid',str(year)]
        Murcia = ['Murcia',str(year)]
        Navarra = ['Navarra',str(year)]
        PaisVasco = ['Pais Vasco',str(year)]
        Rioja = ['La Rioja',str(year)]
        Ceuta = ['Ceuta',str(year)]
        Melilla = ['Melilla',str(year)]
        CeutaMelilla = ['CeutaMelilla',str(year)]
        IDTotal = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/02006.px")
        if (str(IDTotal.status_code) == "200") :
            IDTotaljson = IDTotal.json()
            GastosIntTot = ", Gastos internos (miles de euros): Total"
            GastoIntPor = ", Gastos internos (miles de euros): %"
            Nacional.append(encontrar(IDTotaljson,"Total",GastosIntTot))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastosIntTot))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastosIntTot))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastosIntTot))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastosIntTot))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastosIntTot))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastosIntTot))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastosIntTot))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastosIntTot))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastosIntTot))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastosIntTot))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastosIntTot))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastosIntTot))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastosIntTot))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastosIntTot))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastosIntTot))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastosIntTot))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastosIntTot))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastosIntTot))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastosIntTot))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastosIntTot))

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))
    
        else :
            print(str(year)+"Has no information")

            Nacional.append("")
            Andalucia.append("")
            Aragon.append("")
            Asturias.append("")
            Baleares.append("")
            Canarias.append("")
            Cantabria.append("")
            CastillaLeon.append("")
            CastillaMancha.append("")
            Catalunya.append("")
            Valencia.append("")
            Extremadura.append("")
            Galicia.append("")
            Madrid.append("")
            Murcia.append("")
            Navarra.append("")
            PaisVasco.append("")
            Rioja.append("")
            CeutaMelilla.append("")
            Ceuta.append("")
            Melilla.append("")
    

# GASTO EN I+D SECTOR ADMINISTRACIÓN PÚBLICA. Miles de euros y % DE GASTO I+D ADMINISTRACIÓN # PÚBLICA SOBRE EL TOTAL NACIONAL
        IDAdPub = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07003.px")
        if (str(IDAdPub.status_code) == "200") :
            IDAdPubjson = IDAdPub.json()
            IDTotaljson = IDAdPubjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            Nacional.append("")
            Andalucia.append("")
            Aragon.append("")
            Asturias.append("")
            Baleares.append("")
            Canarias.append("")
            Cantabria.append("")
            CastillaLeon.append("")
            CastillaMancha.append("")
            Catalunya.append("")
            Valencia.append("")
            Extremadura.append("")
            Galicia.append("")
            Madrid.append("")
            Murcia.append("")
            Navarra.append("")
            PaisVasco.append("")
            Rioja.append("")
            CeutaMelilla.append("")
            Ceuta.append("")
            Melilla.append("")
    


# GASTO EN I+D ENSEÑANZA SUPERIOR.Miles de Euros y %Gasto I+D Enseñanza superior sobre el nacional
        IDEnSup = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07004.px")
        if (str(IDEnSup.status_code) == "200") :
            IDEnSupjson = IDEnSup.json()
            IDTotaljson = IDEnSupjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            Nacional.append("")
            Andalucia.append("")
            Aragon.append("")
            Asturias.append("")
            Baleares.append("")
            Canarias.append("")
            Cantabria.append("")
            CastillaLeon.append("")
            CastillaMancha.append("")
            Catalunya.append("")
            Valencia.append("")
            Extremadura.append("")
            Galicia.append("")
            Madrid.append("")
            Murcia.append("")
            Navarra.append("")
            PaisVasco.append("")
            Rioja.append("")
            CeutaMelilla.append("")
            Ceuta.append("")
            Melilla.append("")
            

# GASTO EN I+D SECTOR EMPRESAS. Miles de euros y % DE GASTO I+D EMPRESAS SOBRE EL TOTAL #NACIONAL
        IDemp = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07002.px")
        if (str(IDemp.status_code) == "200") :
            IDempjson = IDemp.json()
            IDTotaljson = IDempjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            Nacional.append("")
            Andalucia.append("")
            Aragon.append("")
            Asturias.append("")
            Baleares.append("")
            Canarias.append("")
            Cantabria.append("")
            CastillaLeon.append("")
            CastillaMancha.append("")
            Catalunya.append("")
            Valencia.append("")
            Extremadura.append("")
            Galicia.append("")
            Madrid.append("")
            Murcia.append("")
            Navarra.append("")
            PaisVasco.append("")
            Rioja.append("")
            CeutaMelilla.append("")
            Ceuta.append("")
            Melilla.append("")

# GASTO EN I+D SECTOR IPSFL Y % DE GASTO I+D  IPSFL SOBRE EL TOTAL NACIONAL
        IDIPSFL = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/07002a.px")
        if (str(IDIPSFL.status_code) == "200") :
            IDIPSFLjson = IDIPSFL.json()
            IDTotaljson = IDIPSFLjson
            GastoIntPor = ", Gastos internos (miles de euros)"

            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            GastoIntPor = ", Gastos internos (%)"
            Nacional.append(encontrar(IDTotaljson,"Total",GastoIntPor))
            Andalucia.append(encontrar(IDTotaljson,"Andalucía",GastoIntPor))
            Aragon.append(encontrar(IDTotaljson,"Aragón",GastoIntPor))
            Asturias.append(encontrar(IDTotaljson,"Asturias (Principado de)",GastoIntPor))
            Baleares.append(encontrar(IDTotaljson,"Baleares (Islas)",GastoIntPor))
            Canarias.append(encontrar(IDTotaljson,"Canarias",GastoIntPor))
            Cantabria.append(encontrar(IDTotaljson,"Cantabria",GastoIntPor))
            CastillaLeon.append(encontrar(IDTotaljson,"Castilla y León",GastoIntPor))
            CastillaMancha.append(encontrar(IDTotaljson,"Castilla - La Mancha",GastoIntPor))
            Catalunya.append(encontrar(IDTotaljson,"Cataluña",GastoIntPor))
            Valencia.append(encontrar(IDTotaljson,"Comunidad Valenciana",GastoIntPor))
            Extremadura.append(encontrar(IDTotaljson,"Extremadura",GastoIntPor))
            Galicia.append(encontrar(IDTotaljson,"Galicia",GastoIntPor))
            Madrid.append(encontrar(IDTotaljson,"Madrid (Comunidad de)",GastoIntPor))
            Murcia.append(encontrar(IDTotaljson,"Murcia (Región de)",GastoIntPor))
            Navarra.append(encontrar(IDTotaljson,"Navarra (Comunidad Foral)",GastoIntPor))
            PaisVasco.append(encontrar(IDTotaljson,"País Vasco",GastoIntPor))
            Rioja.append(encontrar(IDTotaljson,"Rioja (La)",GastoIntPor))
            CeutaMelilla.append(encontrar(IDTotaljson,"Ceuta y Melilla",GastoIntPor))
            Ceuta.append(encontrar(IDTotaljson,"Ceuta",GastoIntPor))
            Melilla.append(encontrar(IDTotaljson,"Melilla",GastoIntPor))

            
        else :
            print(str(year)+"Has no information")
            Nacional.append("")
            Andalucia.append("")
            Aragon.append("")
            Asturias.append("")
            Baleares.append("")
            Canarias.append("")
            Cantabria.append("")
            CastillaLeon.append("")
            CastillaMancha.append("")
            Catalunya.append("")
            Valencia.append("")
            Extremadura.append("")
            Galicia.append("")
            Madrid.append("")
            Murcia.append("")
            Navarra.append("")
            PaisVasco.append("")
            Rioja.append("")
            CeutaMelilla.append("")
            Ceuta.append("")
            Melilla.append("")
            
# Porcentaje de gastos en I+D respecto al PIB a precios de mercado por comunidades autónomas. Serie 2003-2016
        IDPorcPIB = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/02007.px")
        if (str(IDPorcPIB.status_code) == "200") :
            IDPorcPIBjson = IDPorcPIB.json()
        else :
            print(str(year)+"Has no information")

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
            employee_writer.writerow(CeutaMelilla)
            employee_writer.writerow(Ceuta)
            employee_writer.writerow(Melilla)

# Phase3) Transfer csv to Database

        



#with open ('employee_file.csv',mode='w') as employee_file :
    #employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
    #employee_writer.writerow(['John','Accounting','November'])






