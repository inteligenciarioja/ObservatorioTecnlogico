# coding=utf-8
import time
import random
import datetime
import telepot
import os
import subprocess
import randompwd
import smtplib
import request
from telepot.loop import MessageLoop
import requests
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def handl(msg):
	chat_id = msg['chat']['id']
        command = msg['text']
        content_type, chat_type, chat_id  = telepot.glance(msg)
        print(content_type,chat_type,chat_id,command)
	if command == '/time508'
		# 1) Perform query
		req = request.get('https://www.zaragoza.es/sede/servicio/urbanismo-infraestructuras/transporte-urbano/poste-autobus/tuzsa-508?rf=html&srsname=wgs84')
				
	else : 
		bot.sendMessage(chat_id,'This command does not exist')

token = ''
email ="rmcochi@gmail.com"
b = "Raspmovil93@"
#server = smtplib.SMTP('smtp.gmail.com',587)
#print('Introducing token')
bot = telepot.Bot(token)
#print('getme')
bot.getMe()
#print('Gestiono mensajes')
MessageLoop(bot,handle).run_as_thread()
#print ('I am listening')

while 1:
        time.sleep(10)

