import requests
import time
import ssl
from codaio import Coda
from bs4 import BeautifulSoup

API_KEY = 'c5d228f1-a38e-4956-b6e6-f6ceaac089d0'
docid = "G6ody-h41g"
tabid = "grid-k4UzD4Cfru"
titleid = "c-InkHjwP4Lj"
summaryid = "c-tWtHjlDqYt"
interesanteid = "c-F-FPRcC4M7"
intwords = ["ingeniero","telecomunicaciones","terapeuta","ocupacional","concurso","oposición"]

# Hacemos la petición a BOR La Rioja
fecha =  time.strftime("%Y/%m/%d", time.gmtime())
#fecha = '2019/10/09'
url = "https://ias1.larioja.org/boletin/ExportarBoletinServlet?tipo=1&fecha=" + fecha
response = requests.get(url)
#print(response.text)
#print(response.content)

# Hacemos el parseo del XML
soup = BeautifulSoup(response.content, 'xml')
titsoup = soup.find_all('titulo')

# Empezamos con la integración con CODA
coda = Coda(API_KEY)

for i in range (0,len(titsoup)) :
    entries_interesante = "false"
    entries_title = titsoup[i].text
    for c in range (0,len(intwords)):
        if(str(entries_title).lower().find(intwords[c])>=0):
            entries_interesante = "true"
        payload = {
            'rows': [
                {
                    'cells': [
                        {'column': titleid, 'value': entries_title},
                        {'column': interesanteid, 'value':entries_interesante}
                    ],
                },
            ],
            "keyColumns" : [
                titleid
            ]
        }
        try:
            coda.upsert_row(docid,tabid,payload)
        except:
            pass

