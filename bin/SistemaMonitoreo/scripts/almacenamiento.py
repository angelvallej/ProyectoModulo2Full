#!/usr/bin/python

import psutil
import os
from prettytable import PrettyTable
from psutil import virtual_memory

print("\n<h3>#####################\nMonitoreo de Almacenamiento\n####################</h3>")
tabla = PrettyTable(['RAM Total (Bytes)','RAM  Libre (Bytes)','CPU Usado (%)','CPU Libre (%)'])


f = os.popen ("df -h")
for i in f.readlines():
    print i

   

mem = virtual_memory()

x = mem.total
w = mem.free
y = psutil.cpu_percent()
z = 100 - y

#print "||||||||||||Memoria RAM total", x
#print "||||||||||||Memoria RAM disponible", w
#print "||||||||||||CPU en uso (%)",y
#print "|||||||||||CPU disponible (%)", z


print("\n###########################\nMonitoreo de Almacenamiento\n###########################")
tabla = PrettyTable(['RAM Total (Bytes)','RAM  Libre (Bytes)','CPU Usado (%)','CPU Libre (%)'])





