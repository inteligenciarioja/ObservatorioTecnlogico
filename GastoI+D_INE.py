# Prueba de concepto

# Example for DATOS INE I+D
# Python scritp for asking INE API for Cifra de negocios del total de empresas (Incluye los Sectores manufactureros de alta y media-alta tecnología y los servicios de alta tecnología)
# https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/DCC50?nult=10

import requests
import json
from pprint import pprint

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
# GASTO EN I+D TOTAL. Miles de Euros y % GASTO EN I+D TOTAL EN % SOBRE TOTAL NACIONA
for year in range (2000,2019) :
	print ("-----------------------------------------------------------------")
	IDTotal = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a"+str(year)+"/l0/02006.px")
	print ( str(year))
	print(IDTotal.status_code)
	if (str(IDTotal.status_code) == "200") :
		IDTotaljson = IDTotal.json()
		for i in range (0, len(IDTotaljson)) :
			print (IDTotaljson[i]["Nombre"])
			print(IDTotaljson[i] ["Data"] [0] ["Valor"])
	else :
		print ("This year has no information")

# GASTO EN I+D SECTOR ADMINISTRACIÓN PÚBLICA. Miles de euros y % DE GASTO I+D ADMINISTRACIÓN # PÚBLICA SOBRE EL TOTAL NACIONAL
IDAdPub = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/07003.px")
IDAdPubjson = IDAdPub.json()

# GASTO EN I+D ENSEÑANZA SUPERIOR.Miles de Euros y %Gasto I+D Enseñanza superior sobre el nacional
IDEnSup = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/07004.px")
IDEnSupjson = IDEnSup.json()

# GASTO EN I+D SECTOR EMPRESAS. Miles de euros y % DE GASTO I+D EMPRESAS SOBRE EL TOTAL #NACIONAL
IDemp = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/07002.px")
IDempjson = IDemp.json()

# GASTO EN I+D SECTOR IPSFL Y % DE GASTO I+D  IPSFL SOBRE EL TOTAL NACIONAL
IDIPSFL = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/07002a.px")
IDIPSFLjson = IDIPSFL.json()

# Porcentaje de gastos en I+D respecto al PIB a precios de mercado por comunidades autónomas. Serie 2003-2016
IDPorcPIB = requests.get("http://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/t14/p057/a2017/l0/02007.px")
IDPorcPIBjson = IDPorcPIB.json()

# Phase 2) Connect & Insert information in Database












