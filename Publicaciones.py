#PRODUCCIÓN CIENTÍFICA: Fuente Principal FECYT

#Número total de documentos publicados
#http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=98&idPanel=1

#Índice de Impacto Normalizado:
#http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=100&idPanel=1

#% de Publicaciones en revistas del Q1
#http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=99&idPanel=1

#% de Publicaciones en colaboración internacional sobre el total
#http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=114&idPanel=1

#Gasto I+D/Nº Documentos
#http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=174&idPanel=1

 
#NºDocumentos/NºInvestigadores
#http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=174&idPanel=1

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
#Número total de documentos publicados
#http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=98&idPanel=1

browser.delet_all_cookies()
browser.get("http://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=98&idPanel=1")
select1 = Select(browser.find_element_by_id('FiltroInicial:desplegableModalidad'))
select1.select_by_value('W')

