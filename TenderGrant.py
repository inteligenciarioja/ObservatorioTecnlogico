import requests
import csv
from pprint import pprint
import unicodedata as ud
from datetime import datetime
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import MySQLdb
import pandas as pd
from pyvirtualdisplay import Display
#CREATE TABLE ProyEuropeos(Title varchar(100), Id varchar(50) primary key, Deadline varchar(20), status varchar(30), tags varchar(200), keyboards varchar(200));
def limpiarBD() :
    dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
    querystringlimp = "DELETE FROM exampledb.ProyEuropeo"
    c = dbconnection.cursor()
    c.execute(querystringlimp)
    dbconnection.commit()
    c.close()
    dbconnection.close()
    
def incluirBD(listainc) :
    straux = "','".join(listainc)
    strauxfinal = "'"+straux+"'"
        
    querystringa = """INSERT INTO exampledb.ProyEuropeos (title , Id, Deadline, status, tags, keyboards) VALUES ("""+ strauxfinal + """) ON DUPLICATE KEY UPDATE status = 'chequeado';"""
    querystring = querystringa.encode('ascii','ignore')
    #print(querystring)
    dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        
    c = dbconnection.cursor()
    c.execute(querystring)
    dbconnection.commit()
    c.close()
    dbconnection.close()
    
url = "http://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json"
response = requests.get("http://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json")
rjson = response.json()
#pprint(rjson)
#print(str((rjson ["fundingData"]["GrantTenderObj"][0]["callTitle"])))
#print(str((rjson ["fundingData"]["GrantTenderObj"][0]["identifier"])))
#print(str((rjson ["fundingData"]["GrantTenderObj"][0]["publicationDateLong"])))
#print(str((rjson ["fundingData"]["GrantTenderObj"][0]["plannedOpeningDateLong"])))
#print(str((rjson ["fundingData"]["GrantTenderObj"][0]["deadlineDatesLong"][0])))
#print(str((rjson ["fundingData"]["GrantTenderObj"][0]["frameworkProgramme"]["description"])))
#print(str((rjson ["fundingData"]["GrantTenderObj"][0]["status"]["abbreviation"])))

lista = []
lista2= []
listatitle = []

with open ('Trend&Grants.csv',mode='w') as employee_file :
        employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Project','Id','DeadlineDate','Status','tags','keywords'])
for i in range (0, len(rjson ["fundingData"]["GrantTenderObj"])) :
    if (rjson ["fundingData"]["GrantTenderObj"][i]["status"]["abbreviation"] != "Closed" and i != 4050) :
        print(i)
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["callTitle"])))
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["identifier"])))
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["publicationDateLong"])))
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["plannedOpeningDateLong"])))
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["deadlineDatesLong"][0])))
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["frameworkProgramme"]["description"])))
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["status"]["abbreviation"])))
        #print(str((rjson ["fundingData"]["GrantTenderObj"][i]["workProgrammepart"]["wp_website"])))
        #lista.append(ud.normalize('NFC',str((rjson ["fundingData"]["GrantTenderObj"][i]["callTitle"]))))
        lista.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["title"])).encode('ascii', 'ignore'))
        lista.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["identifier"])).encode('ascii','ignore'))
        #lista.append(ud.normalize('NFC',str((rjson ["fundingData"]["GrantTenderObj"][i]["publicationDateLong"]))))
        #lista.append(ud.normalize('NFC',str((rjson ["fundingData"]["GrantTenderObj"][i]["plannedOpeningDateLong"]))))
        if (len(rjson ["fundingData"]["GrantTenderObj"][i]["deadlineDatesLong"]) == 0) :
            lista.append('-2')
        else :
            lista.append(datetime.fromtimestamp(int(str((rjson ["fundingData"]["GrantTenderObj"][i]["deadlineDatesLong"][0])))/1000.0).strftime("%Y/%m/%d").encode('ascii','ignore'))
        
        #lista.append(ud.normalize('NFC',str((rjson ["fundingData"]["GrantTenderObj"][i]["frameworkProgramme"]["description"]))))
        lista.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["status"]["abbreviation"])).encode('ascii','ignore'))
        #lista.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["workProgrammepart"]["wp_website"])))
        #lista.append(str((rjson ["fundingData"]["GrantTenderObj"][0] ['keywords'])).encode('ascii','ignore'))
        if (str((rjson ["fundingData"]["GrantTenderObj"][i])).find("tags") >= 0) :
            lista.append(str((rjson ["fundingData"]["GrantTenderObj"][i] ['tags'])).encode('ascii','ignore'))
        else :
            lista.append(str('').encode('ascii','ignore'))
        if (str((rjson ["fundingData"]["GrantTenderObj"][i])).find("keywords") >= 0) :
            lista.append(str((rjson ["fundingData"]["GrantTenderObj"][i] ['keywords'])).encode('ascii','ignore'))
        else :
            lista.append(str('').encode('ascii','ignore'))
        with open ('Trend&Grants.csv',mode='a') as employee_file :
            employee_writer = csv.writer(employee_file, delimiter=';',quoting = csv.QUOTE_MINIMAL)
            employee_writer.writerow(lista)
        
        lista2.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["title"])).replace("""'""",''))
        lista2.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["identifier"])).replace("""'""",''))
        if (len(rjson ["fundingData"]["GrantTenderObj"][i]["deadlineDatesLong"]) == 0) :
            lista2.append('-2')
        else :
            lista2.append(datetime.fromtimestamp(int(str((rjson ["fundingData"]["GrantTenderObj"][i]["deadlineDatesLong"][0])))/1000.0).strftime("%Y/%m/%d"))
        lista2.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["status"]["abbreviation"])))
        if (str((rjson ["fundingData"]["GrantTenderObj"][i])).find("tags") >= 0) :
            lista2.append(', '.join(rjson ["fundingData"]["GrantTenderObj"][i] ['tags']).replace("""'""",''))
        else :
            lista2.append(str(''))
        if (str((rjson ["fundingData"]["GrantTenderObj"][i])).find("keywords") >= 0) :
            lista2.append(', '.join(rjson ["fundingData"]["GrantTenderObj"][i] ['keywords']).replace("""'""",''))
        else :
            lista2.append(str(''))
        dbconnection = MySQLdb.connect(host='localhost',db='exampledb',
                              user='exampleuser', passwd='pimylifeup')
        straux1 = """select count(*) from ProyEuropeos WHERE Id = '""" + str((rjson ["fundingData"]["GrantTenderObj"][i]["identifier"])).replace(""""'""",'') + """'"""
        #print(straux1)
        df = pd.read_sql(straux1.replace('–','-'),con = dbconnection)
        print(df ["count(*)"] [0])
        if (df ["count(*)"] [0] == 0) :
            listatitle.append(str((rjson ["fundingData"]["GrantTenderObj"][i]["identifier"]))+ "---" + str((rjson ["fundingData"]["GrantTenderObj"][i]["title"])))
        incluirBD(lista2)
        lista = []
        lista2 = []

# Sacar proyectos en plazo de RED.ES
#display = Display(visible = 0, size = (1024,768))
#display.start()
#browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#browser.get('https://sede.red.gob.es/procedimientos')
#element = browser.find_element_by_class_name("titulo")


auxstr = '\n-----------------------------------\n'.join(listatitle)
# Enviar enlaces de interés y el fichero con los abiertos e interesantes y si hubiera alguno nuevo
subject = "European and National Project Review"
body = ("""Estos son los enlaces a proyectos más interesantes:
RED.ES
https://sede.red.gob.es/procedimientos""" + """\n""" 

"""\nCDTI
https://www.cdti.es/index.asp?MP=1&MS=0&MN=1&r=1920*1080

y los proyectos europeos nuevos son:
"""+ auxstr)

#print(body)
sender_email = "mcochirodrioja@gmail.com"
receiver_email = "mcochi@larioja.org"
password = "Fombera2019"

#Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email

#Add body to email
message.attach(MIMEText(body,"plain"))
filename = "Trend&Grants.csv"

with open (filename, "rb") as attachment:
    part = MIMEBase("application","octet-stream")
    part.set_payload(attachment.read())
#Encode file in ASCII
encoders.encode_base64(part)

part.add_header("Content-Disposition","attachment; filename= Trend&Grants.csv",)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    server.sendmail(sender_email,"amartintezf@larioja.org",text)	
