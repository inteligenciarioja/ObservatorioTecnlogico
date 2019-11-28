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

# Py script for sending automatic emails informing about correct behaviour

email ="rmcochi@gmail.com"
b = "Raspmovil93!"
toemail= "jcochimonzon2@gmail.com"
s = smtplib.SMTP("smtp.gmail.com:587")
s.ehlo()
s.starttls()
s.login(email,b)
#Send the mail  
msg = "Para ver los videos de la cámara de vigilancia conectarse a rmcochi.ddns.net con FileZilla en el directorio /mnt/video/ Recuerda conectarte primero a la VPN y que los videos se borran tras 48 horas"
s.sendmail(email,email,msg)
s.sendmail(email,toemail,msg)
s.quit()

