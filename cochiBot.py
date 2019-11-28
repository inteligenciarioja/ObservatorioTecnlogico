# coding=utf-8
import time
import random
import datetime
import telepot
import os
import subprocess
import randompwd
import smtplib
from telepot.loop import MessageLoop

pwd = randompwd.randomString()
def handle(msg):
	global pwd
	global mail
	global b
	print(pwd)
	chat_id = msg['chat']['id']
	command = msg['text']
	content_type, chat_type, chat_id  = telepot.glance(msg)
	print(content_type,chat_type,chat_id,command)
	if command == '/time':
		bot.sendMessage(chat_id,subprocess.check_output('date').decode("utf-8"))
	elif command == '/stats':
		bot.sendMessage(chat_id,subprocess.check_output('df').decode("utf-8"))
	elif command == '/videos':
		bot.sendMessage(chat_id,subprocess.check_output(['ls','-t','/mnt/video/']).decode("utf-8"))	
	elif command == '/lastfour':
		#sentence = "find /mnt/video/*.h264 -mmin -59 -exec cp {} /root/rmcochi\@gmail.com/ \;"
		#print("Uploading!!!!")
		#Genero la contraseña aleatoria
		pwd = randompwd.randomString()
		#send mail to my mail
		s = smtplib.SMTP("smtp.gmail.com:587")
		s.ehlo()
		s.starttls()
		s.login(email,b)
		#Send the mail
		msg = pwd
		s.sendmail(email,email,msg)
		s.quit()
		bot.sendMessage(chat_id,"El identificador ha sido enviado")
	elif command == pwd:
		pwd = randompwd.randomString()
		bot.sendMessage(chat_id,"Uploading!!!!")
		subprocess.check_output("/home/pi/./lastfour.sh")
		subprocess.check_output("/home/pi/./sync.sh")
		bot.sendMessage(chat_id,"Videos have been uploaded")
		#bot.sendMessage(chat_id, "https://drive.google.com/open?id=1zMcnQu20qmq6cJ3KSWTe0Nm8QRG3jbJE")
		bot.sendMessage(chat_id,"Recuerda que la carga no es inmediata, es necesario esperar unos minutos hasta que todo se refresca")
		pwd = randompwd.randomString()
	else:
		bot.sendMessage(chat_id,'This command does not exist')
token = '666171967:AAHMYr-kf0S7_ObWzDaSo08nEVHnyKrbYo0'
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
