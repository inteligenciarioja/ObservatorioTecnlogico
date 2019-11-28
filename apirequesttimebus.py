# coding=utf-8
import time 
import random 
import datetime
import telepot
import os 
import subprocess
import randompwd
import smtplib 
import requests
import json
from collections import namedtuple
from telepot.loop import MessageLoop

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

# Python scritp for requesting arrive time for urban buses in Zaragoza
payload ={'Accept':'application/json','Content-Type':'application/json; charset=UTF-8'} 
t = requests.get('http://www.zaragoza.es/api/recurso/urbanismo-infraestructuras/transporte-urbano/poste/tuzsa-508',headers=payload) 
print("Texto")
print(t.text)
print("Ya ha json")
print(t.json())
print(t.status_code)
if t.status_code == 200 :
	#print(t.json())
	# Next, we'll process Json, transferring info to python object
	# Convert to JSONOBJECT
	bustime = json2obj(t.text)
	#print(bustime.title.type.Point.Coordinates)
else:
	print("Something was wrong")
	print(t.text)
