#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

#Strings deklarieren
strJahr = strMonat = strOrdnername = "."

# zeit auslesen
now = time.localtime()

#Jahr und Monat auslesen
strJahr = str(now.tm_year)
strMonat = str(now.tm_mon)

# ordnernamen zusammenbauen
strOrdnername = strJahr + "." + strMonat

# ausgabe des ornernamens
print ("der ordnername: ", strOrdnername)

sPfad = "c:\\temp\\python\\Testordner\\" + strOrdnername
print 

if os.path.exists(sPfad) == True:
    print(sPfad, "existiert.")
else:
    print(sPfad, "existiert nicht.")
    os.mkdir(sPfad)
