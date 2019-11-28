# Prueba de concepto

# Example for DATOS OEPM
# Python scritp for asking OEPM Data


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import shutil
import os
import csv
import json

def encontrarrango(reader):
    maxyear = 2002
    listayear = []
    for row in reader :
        listayear.append(int(row["columna"]))
    maxyear = max(int(s) for s in listayear)
    print(maxyear)
    return maxyear
source = []

def encontrarnac( reader, year):
    ind = "-2"
    for row in reader:
        #print(row['columna'])
        #print(row['subcolumna'])
        if (row['columna'].find(str(year)) >= 0):
            if (row['subcolumna'].find("EXPORT") >= 0):
                ind = row['valor']
    return ind

def tojson(file):
    #Open csv
    with open(file,mode='r') as csv_file:
        reader = csv.DictReader(csv_file,delimiter=',')
        jsonout = json.dumps([row for row in reader])
        print(jsonout)
    return jsonout

with open ('Contexto4.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(["Region","year","date","id","Export"])
        
# Preparamos el Browser que vamos a utlizar
#Chromium
#display = Display(visible = 1, size=(800,800))
#display.start()
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--window-size=1420,1080')
#chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')#,chrome_options=chrome_options)


# ---------------------------------------------------------------------------------------------------
# PRUEBA EXTRACCIÓN INFORMACIÓN OFICINA ESPAÑOLA DE PATENTES Y MARCAS
#browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.delete_all_cookies()
driver.get("http://datacomex.comercio.es/principal_comex_es.aspx")


#browser.find_element_by_class_name("botonInicio").click()
#En nuestro caso los elementos están embebidos en un iframe, y hay que hacer un cambio
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
# 1) Vamos al modo avanzado
driver.find_element_by_id("irAvanzado").click()
# 2) Seleccionamos los valores de filas
time.sleep(5)
select1 = Select(driver.find_element_by_id('DimFilas'))
select1.select_by_visible_text('Territorial')
# 3) Seleccionamos los valores de columanas
select2 = Select(driver.find_element_by_id('DimColumnas'))
select2.select_by_visible_text('Fechas')

# 4) Generamos el infomre
driver.find_element_by_id("enviarDatos").click()

# 5) Le damos a fechas para que nos de más detalle
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#a = driver.find_elements(By.XPATH,'//a')
driver.find_element_by_xpath("//a[@tabindex='3']").click()

# 6) En este momento ya nos podemos bajar el total nacional
time.sleep(5)
#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#a = driver.find_elements(By.XPATH,'//div')
driver.find_element_by_xpath("//div[@id='oCMenu_Exportar_0']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@id='oCMenu_ExportarCSV']").click()
time.sleep(10)
sourceaux = os.listdir("/home/pi/Downloads")
for file in sourceaux:
    if file.startswith("DataComex"):
        shutil.move("/home/pi/Downloads/"+file,"/home/pi/Desktop/Contexto/nacional.csv")


# 7) Le damos ahora a Total Nacional
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#a = driver.find_elements(By.XPATH,'//a')
driver.find_element_by_xpath("//a[@tabindex='154']").click()

# 8) Nos descargamos el fichero
time.sleep(5)
#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#a = driver.find_elements(By.XPATH,'//div')
driver.find_element_by_xpath("//div[@id='oCMenu_Exportar_0']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@id='oCMenu_ExportarCSV']").click()
time.sleep(10)
sourceaux = os.listdir("/home/pi/Downloads")
for file in sourceaux:
    if file.startswith("DataComex"):
        shutil.move("/home/pi/Downloads/"+file,"/home/pi/Desktop/Contexto/ccaa.csv")


time.sleep(10)
driver.quit()

# Ahora empezamos a procesar tanto el fichero nacional como el de comunidades autónomas

with open('nacional.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file,delimiter=',')
    rango = encontrarrango(csv_reader)
    
for j in range (2002, rango) :
    fecha = time.strftime("%Y-%m-%d", time.gmtime())
    Nacional = ['Nacional',str(rango),fecha, 'Nacional' + str(rango)]
    with open('nacional.csv',mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file,delimiter=',')
        Nacional.append(encontrarnac( csv_reader, j))
        print(Nacional)
#Vamos a pasar ambos archivos a json, porque sino tenemos que cerrarlo y abrirlo cada vez
#jsonnacional = tojson('nacional.csv')
#jsonccaa = tojson('ccaa.csv')

    #for j in range(2002,rango):
        #year = str(j)
        #fecha = time.strftime("%Y-%m-%d", time.gmtime())
        #Nacional = ['Nacional',str(year),fecha, 'Nacional' + str(year)]
        #Andalucia = ['Andalucía',str(year), fecha, 'Andalucía' + str(year)]
        #Aragon = ['Aragón',str(year), fecha, 'Aragón' + str(year)]
        #Asturias = ['Asturias',str(year), fecha, 'Asturias' + str(year)]
        #Baleares = ['Balears',str(year), fecha, 'Balears' + str(year)]
        #Canarias = ['Canarias',str(year), fecha, 'Canarias' + str(year)]
        #Cantabria = ['Cantabria',str(year), fecha, 'Cantabria' + str(year)]
        #CastillaLeon = ['Castilla y León',str(year), fecha, 'Castilla y León' + str(year)]
        #CastillaMancha = ['Castilla - La Mancha',str(year), fecha, 'Castilla - La Mancha' + str(year)]
        #Catalunya = ['Cataluña',str(year), fecha, 'Cataluña' + str(year)]
        #Valencia = ['Comunitat Valenciana',str(year), fecha, 'Valencia' + str(year)]
        #Extremadura = ['Extremadura',str(year), fecha, 'Extremadura' + str(year)]
        #Galicia = ['Galicia',str(year), fecha, 'Galicia' + str(year)]
        #Madrid = ['Madrid',str(year), fecha, 'Madrid' + str(year)]
        #Murcia = ['Murcia',str(year), fecha, 'Murcia' + str(year)]
        #Navarra = ['Navarra',str(year), fecha, 'Navarra' + str(year)]
        #PaisVasco = ['País Vasco',str(year), fecha, 'País Vasco' + str(year)]
        #Rioja = ['Rioja',str(year), fecha, 'Rioja' + str(year)]
        #Ceuta = ['Ceuta',str(year), fecha, 'Ceuta' + str(year)]
        #Melilla = ['Melilla',str(year), fecha, 'Melilla' + str(year)]
        #CeutaMelilla = ['CeutaMelilla',str(year), fecha, 'CeutaMelilla' + str(year)]
        #lista = [Nacional,Andalucia,Aragon, Asturias, Baleares, Canarias, Cantabria, CastillaLeon, CastillaMancha, Catalunya, Valencia, Extremadura, Galicia, Madrid, Murcia, Navarra, PaisVasco, Rioja, Ceuta, Melilla]
        #with open('Contexto4.csv',mode='a') as employee_file :
        #    employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        #    lista[0].append(encontrarnac(lista[0][0], csv_reader, year))
        #    print(lista[0])
        #    employee_writer.writerow(lista[0])









