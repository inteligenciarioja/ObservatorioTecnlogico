# Transferencia a CODA de Contexto2.py
import csv
from codaio import Coda
import ssl


API_KEY = ''
docid="G6ody-h41g"
tabid = "grid-r2hvl_u-eJ"
columnid = "c-JLQHCL5TG3"
columnind = "c-eonKWhVyeD"
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

coda = Coda(API_KEY)

with open ('Contexto2.csv',mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        #print(row)
        payload = {
                        'rows': [
                        {   
                    'cells': [
                        {'column': columnid, 'value': row["id"]},
                        {'column': columnind, 'value':row["EmpxHab"]}
                        ],
                        },
                        ],
                    "keyColumns" : [
                        columnid
                        ]
        }
        coda.upsert_row(docid,tabid,payload)
