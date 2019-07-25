from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

import os

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
browser = webdriver.Safari()
#Para Javascript <img id="btnTabla" class="iconoIndicadores imgBoton" src="/SiteAssets/imgs/tabla.gif" onclick="btnTabla_click();" width="16" height="16" alt="Ver Tabla de Datos" title="Ver Tabla de Datos">
#Para CSV <img id="btnCsv" class="iconoIndicadores imgBoton" src="/SiteAssets/imgs/excel.gif" onclick="btnCsv_click();" width="16" height="16" alt="Exportar datos a excel" title="Exportar datos a excel"><img id="btnCsv" class="iconoIndicadores imgBoton" src="/SiteAssets/imgs/excel.gif" onclick="btnCsv_click();" width="16" height="16" alt="Exportar datos a excel" title="Exportar datos a excel">

browser.get("https://services.icono.fecyt.es/indicadores/Paginas/default.aspx?ind=98&idPanel=1")
print("Voy a intentar encontrar en elemento")
browser.find_element_by_id("btnCsv").click()
html = browser.page_source
print(html)
                    
#browser.get("http://google.com")
browser.implicitly_wait(10)

browser.quit()

browser = webdriver.Safari()
browser.get("http://consultas2.oepm.es/ipstat/faces/IpsBusqueda.xhtml")
'''
<select id="FiltroInicial:desplegableModalidad" name="FiltroInicial:desplegableModalidad" class="txt w_320" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:desplegableTipoEstadistica FiltroInicial:desplegableEstadistica FiltroInicial:panelCriterios')">	<option value="" selected="selected">-- seleccione Indicador de Modalidad --</option>
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
print(select1.options)
select1.select_by_visible_text('2. Patentes Vía Nacional')

'''
<select id="FiltroInicial:desplegableTipoEstadistica" name="FiltroInicial:desplegableTipoEstadistica" class="txt w_320" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:desplegableEstadistica FiltroInicial:panelCriterios')">	<option value="">-- seleccione Tipo --</option>
	<option value="3">SOLICITUDES PRESENTADAS</option>
	<option value="4">SOLICITUDES PUBLICADAS</option>
	<option value="5">CONCESIONES</option>
	<option value="6">EN VIGOR</option>
</select>
'''
wait = WebDriverWait(browser,10)
time.sleep(5)
element = wait.until(EC.visibility_of_element_located((By.ID,'FiltroInicial:desplegableTipoEstadistica')))
select2 = Select(browser.find_element_by_id('FiltroInicial:desplegableTipoEstadistica'))
print(select2.options)
select2.select_by_value('4')
'''
<select id="FiltroInicial:desplegableEstadistica" name="FiltroInicial:desplegableEstadistica" class="txt w_540" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:panelCriterios')">	<option value="">-- seleccione Estadistica --</option>
	<option value="16">1. Solicitudes de Patentes publicadas por Sectores Técnicos y distribuidas por CC.AA. </option>
	<option value="17">2. Solicitudes de Patentes publicadas por Subsectores Técnicos y distribuidas por provincias</option>
	<option value="18">3. Distribución en porcentaje de los Sectores Técnicos de las solicitudes publicadas de Patentes</option>
	<option value="35">4. Solicitudes de Patentes publicadas por Unidades Técnicas y clases CIP, distribuidas por CC.AA.</option>
	<option value="36">5. Solicitudes de Patentes publicadas por Unidades Técnicas y clases CIP, distribuidas por provincias</option>
</select>
'''
wait = WebDriverWait(browser,10)
time.sleep(5)
select3 = Select(browser.find_element_by_id('FiltroInicial:desplegableEstadistica'))
print(select3.options)
browser.find_element_by_id("FiltroInicial:desplegableEstadistica").click()
wait = WebDriverWait(browser,10)
select3.select_by_value('17')
'''
<select id="FiltroInicial:anualidadDesde" name="FiltroInicial:anualidadDesde" class="txt w_50" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:anualidadHasta')">	<option value="2009" selected="selected">2009</option>
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
time.sleep(5)
browser.implicitly_wait(10)
select4 = Select(browser.find_element_by_id('FiltroInicial:anualidadDesde'))
select4.select_by_value('2009')

'''
<select id="FiltroInicial:anualidadHasta" name="FiltroInicial:anualidadHasta" class="txt w_50" size="1" onchange="mojarra.ab(this,event,'valueChange',0,'FiltroInicial:anualidadDesde')">	<option value="2009">2009</option>
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
time.sleep(1)
browser.implicitly_wait(10)
select5 = Select(browser.find_element_by_id('FiltroInicial:anualidadHasta'))
select5.select_by_value('2018')

'''
<input id="FiltroInicial:j_idt73" type="submit" name="FiltroInicial:j_idt73" value="" class="addAll" onclick="mojarra.ab(this,event,'action','FiltroInicial:AutonomiaDesde','FiltroInicial:AutonomiaDesde FiltroInicial:AutonomiaHasta');return false">
'''
time.sleep(1)
browser.implicitly_wait(10)
browser.find_element_by_id("FiltroInicial:j_idt85").click()
'''
<input id="FiltroInicial:j_idt109" type="submit" name="FiltroInicial:j_idt109" value="" class="addAll" onclick="mojarra.ab(this,event,'action','FiltroInicial:STDesde','FiltroInicial:STDesde FiltroInicial:STHasta');return false">
'''
time.sleep(1)
browser.implicitly_wait(10)
browser.find_element_by_id("FiltroInicial:j_idt109").click()
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
time.sleep(20)
print('Ya estoy en la otra página')

'''
element = browser.find_element_by_id('btnExport__')
element.click()
'''
a = browser.find_element_by_id("btnExport__")
a.click()
browser.quit()
