# Prueba de concepto

# Example for DATOS OEPM
# Python scritp for asking OEPM Data


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from lxml import etree
import pandas as pd
import shutil
import time
import os
import csv

import MySQLdb
import time

def incluirBD(df, year) :
    # CREATE TABLE SOLPCTHAB(CCAA varchar(30), Solicitudes varchar(30), VarAnual varchar(30), PorcSobreTotalES varchar(30), Nhabitantes varchar(30), PorcHabitantesfrentetotalES varchar(30),RatioSolMillonHab varchar(30), DesviacionMedida varchar(30),Year varchar(30));
    header = df.iloc[0]
    fecha = time.strftime("%Y-%m-%d", time.gmtime())
    for i in range(1, df.shape[0]) :
        row = df.iloc[i]
        final = float(df.shape[0])
        porcentaje = (float(i)/final)*100
        print(str(i) + str(year) + str(porcentaje))
        lista = row.values.tolist()
        lista.append(str(year))
        listafinal = [str(item) for item in lista]
        straux = "','".join(listafinal)
        strauxfinal = "'"+straux+"'"
        querystring = ("""INSERT INTO exampledb.SOLPCTHAB"""
            """(CCAA, Solicitudes, VarAnual, PorcSobreTotalES,  """
            """Nhabitantes, PorcHabitantesfrentetotalES,"""
            """RatioSolMillonHab, DesviacionMedida, Year)"""
                       """ VALUES (""" + strauxfinal + """ );""")
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
    querystringlimp = "DELETE FROM exampledb.SOLPCTHAB"
    c = dbconnection.cursor()
    c.execute(querystringlimp)
    dbconnection.commit()
    c.close()
    dbconnection.close()

limpiarBD()

with open ('SOL PCT HAB.csv', mode = 'a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=';', quoting = csv.QUOTE_MINIMAL)
        header = ['CC.AA.','Solicitudes','Variacion Anual','% sobre Total ES','Nº Habitantes','% Habitantes/ Total ES','Ratio Solicitudes/ Millon Hab.','Desviación sobre la media','Year']
        employee_writer.writerow(header)
# Configuración del Driver en función del navegador
# Safari
#os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
#browser = webdriver.Safari()
#Para Javascript <img id="btnTabla" class="iconoIndicadores imgBoton" src="/SiteAssets/imgs/tabla.gif" onclick="btnTabla_click();" width="16" height="16" alt="Ver Tabla de Datos" title="Ver Tabla de Datos">
#Para CSV <img id="btnCsv" class="iconoIndicadores imgBoton" src="/SiteAssets/imgs/excel.gif" onclick="btnCsv_click();" width="16" height="16" alt="Exportar datos a excel" title="Exportar datos a excel"><img id="btnCsv" class="iconoIndicadores imgBoton" src="/SiteAssets/imgs/excel.gif" onclick="btnCsv_click();" width="16" height="16" alt="Exportar datos a excel" title="Exportar datos a excel">

#Chromium
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

# Firefox
'''
geckodriver = '/home/pi/Desktop/geckodriver'
options = Options()
options.headless = True
browser = webdriver.Firefox(executable_path=geckodriver, options = options)
'''
# ---------------------------------------------------------------------------------------------------
# PRUEBA EXTRACCIÓN INFORMACIÓN OFICINA ESPAÑOLA DE PATENTES Y MARCAS
#browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
for year in range (2005,2019) :
    browser.delete_all_cookies()
    browser.get("http://consultas2.oepm.es/ipstat/faces/IpsBusqueda.xhtml")
    '''
    <select id="FiltroInicial:desplegableModalidad" name="FiltroInicial:desplegableModalidad" class="txt w_320" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:desplegableTipoEstadistica FiltroInicial:desplegableEstadistica FiltroInicial:panelCriterios')">    <option value="" selected="selected">-- seleccione Indicador de Modalidad --</option>
    <option value="PEE">1. Patentes (Vía Nacional, Vía Europea y Vía PCT)</option>
    <option value="P">2. Patentes Vía Nacional</option>
    <option value="E">3. Patentes Vía Europea</option>
    <option value="W">4. Patentes Vía PCT (Solicitud Internacional de Patente)</option>
    <option value="WBI">5. OEPM como Administración de Búsqueda Internacional</option>
    <option value="T">6. Topografías de Productos Semiconductores</option>
    <option value="C">7. Certificados Complementarios de Protección</option>
    <option value="U">8. Modelo de Utilidad Vía Nacional</option>
    </select>
    '''
    #browser.implicitly_wait(10)
    select1 = Select(browser.find_element_by_id('FiltroInicial:desplegableModalidad'))
    select1.select_by_value('W')
    print(select1.options)

    '''
    <select id="FiltroInicial:desplegableTipoEstadistica" name="FiltroInicial:desplegableTipoEstadistica" class="txt w_320" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:desplegableEstadistica FiltroInicial:panelCriterios')"> <option value="">-- seleccione Tipo --</option>
    <option value="3">SOLICITUDES PRESENTADAS</option>
    <option value="4">SOLICITUDES PUBLICADAS</option>
    <option value="5">CONCESIONES</option>
    <option value="6">EN VIGOR</option>
    </select>
    '''
    wait = WebDriverWait(browser,10)
    time.sleep(1)
    element = wait.until(EC.visibility_of_element_located((By.ID,'FiltroInicial:desplegableTipoEstadistica')))
    select2 = Select(browser.find_element_by_id('FiltroInicial:desplegableTipoEstadistica'))
    print(select2.options)
    select2.select_by_value('20')
    '''
    <select id="FiltroInicial:desplegableEstadistica" name="FiltroInicial:desplegableEstadistica" class="txt w_540" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:panelCriterios')">  <option value="">-- seleccione Estadistica --</option>
    <option value="16">1. Solicitudes de Patentes publicadas por Sectores Técnicos y distribuidas por CC.AA. </option>
    <option value="17">2. Solicitudes de Patentes publicadas por Subsectores Técnicos y distribuidas por provincias</option>
    <option value="18">3. Distribución en porcentaje de los Sectores Técnicos de las solicitudes publicadas de Patentes</option>
    <option value="35">4. Solicitudes de Patentes publicadas por Unidades Técnicas y clases CIP, distribuidas por CC.AA.</option>
    <option value="36">5. Solicitudes de Patentes publicadas por Unidades Técnicas y clases CIP, distribuidas por provincias</option>
    </select>
    '''
    wait = WebDriverWait(browser,10)
    time.sleep(1)
    select3 = Select(browser.find_element_by_id('FiltroInicial:desplegableEstadistica'))
    print(select3.options)
    browser.find_element_by_id("FiltroInicial:desplegableEstadistica").click()
    wait = WebDriverWait(browser,10)
    select3.select_by_value('61')
    '''
    <select id="FiltroInicial:anualidadDesde" name="FiltroInicial:anualidadDesde" class="txt w_50" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:anualidadHasta')">   <option value="2009" selected="selected">2009</option>
    <option value="2010">2010</option>
    <option value="2011">2011</option>
    <option value="2012">2012</option>
    <option value="2013">2013</option>
    <option value="2014">2014</option>
    <option value="2015">2015</option>
    <option value="2016">2016</option>
    <option value="2017">2017</option>
    <option value="2018">2018</option>
    </select>
    '''
    time.sleep(1)
    browser.implicitly_wait(10)
    select4 = Select(browser.find_element_by_id('FiltroInicial:anualidadDesde'))
    select4.select_by_value(str(year))

    '''
    <select id="FiltroInicial:anualidadHasta" name="FiltroInicial:anualidadHasta" class="txt w_50" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:anualidadDesde')">   <option value="2009">2009</option>
    <option value="2010">2010</option>
    <option value="2011">2011</option>
    <option value="2012">2012</option>
    <option value="2013">2013</option>
    <option value="2014">2014</option>
    <option value="2015">2015</option>
    <option value="2016">2016</option>
    <option value="2017">2017</option>
    <option value="2018" selected="selected">2018</option>
    </select>
    '''
    '''
    time.sleep(1)
    browser.implicitly_wait(10)
    select5 = Select(browser.find_element_by_id('FiltroInicial:anualidadHasta'))
    select5.select_by_value('2018')
    '''

    '''
    <input id="FiltroInicial:j_idt73" type="submit" name="FiltroInicial:j_idt73" value="" class="addAll" onclick="mojarra.ab(this,event,'action','FiltroInicial:AutonomiaDesde','FiltroInicial:AutonomiaDesde FiltroInicial:AutonomiaHasta');return false"Hola-mundo.pdf
    '''
    time.sleep(1)
    browser.implicitly_wait(10)
    browser.find_element_by_id("FiltroInicial:j_idt73").click()
    '''
    <input id="FiltroInicial:j_idt109" type="submit" name="FiltroInicial:j_idt109" value="" class="addAll" onclick="mojarra.ab(this,event,'action','FiltroInicial:STDesde','FiltroInicial:STDesde FiltroInicial:STHasta');return false">
    '''
    '''
    time.sleep(1)
    browser.implicitly_wait(10)
    browser.find_element_by_id("FiltroInicial:j_idt109").click()
    '''
    '''
    browser.implicitly_wait(10)
    <input type="submit" name="FiltroInicial:j_idt177" value="Buscar">
    '''
    time.sleep(1)
    browser.implicitly_wait(10)
    browser.find_element_by_name("FiltroInicial:j_idt177").click()                              
                               

    '''f
    <a id="btnExport__" href="javascript:descargarExcel()"> <img title="Exportar a Excel" src="resources/export_excel_icon.jpg">
                </a>'''
    browser.implicitly_wait(10)
    time.sleep(15)
    #print('Ya estoy en la otra página')

    '''
    element = browser.find_element_by_id('btnExport__')
    element.click()
    '''
    browser.find_element_by_id("btnExport__").click()
    time.sleep(10)
    

    #Mover download xml file to current directory, in may case, Desktop
    shutil.move('/home/pi/Downloads/download','/home/pi/Desktop/download')

    #Empezar a procesar el xml file
    html = open('download')
    #print(html.read())

    #Convertir tabla en csv y escribirla en la base de datos
    s = html.read()
    dfs = pd.read_html(s)
    df = dfs[0]
    row = []
    with open ('SOL PCT HAB.csv', mode = 'a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=';', quoting = csv.QUOTE_MINIMAL)
        for i in range (1,df.shape[0]) :
            row =  [df[j][i] for j in range (0,df.shape[1])]
            row.append(str(year))
            employee_writer.writerow(row)
    incluirBD(df, year)
browser.quit()
