#!/usr/bin/python
# -*- coding: utf-8 -*-

#import md5hash
#from md5hash import scan
import os
import sys
import time, locale
import sqlite3
import exifread
    

# hier kann der pfad einer einzelnen datei eingegeben werden um nachzusehen, weshalb das exif read nicht funktioniert, bzw. welche daten extrahiert werden.


#def auslesenOrdnerRekursiv(walk_dir):
#    for root, dirs, files in os.walk(walk_dir, topdown=False):
#        for name in files:


#sDateinameUndPfad = os.path.join(root, name)
#sDateiname = (os.path.join(name))
#sPruefsumme = scan(sDateinameUndPfad)

sDateinameUndPfad = "C:\\01CM\\400 CM\\003_HandyBilder\\2012-05-05 08.10.17.jpg"
sDateinameUndPfad = "C:\\01CM\\400 CM\\003_HandyBilder\\2012-05-05 12.11.05.jpg"


print('---------------------------------------------------------------------------')
print('sDateinameUndPfad  :' + sDateinameUndPfad )  #+ ':      , sDateiname  :' + sDateiname+ ':      und sPruefsumme  :' + sPruefsumme)



f = open(sDateinameUndPfad, 'rb')
tags = exifread.process_file(f)

#try:
print (tags["EXIF DateTimeOriginal"])
print (tags["EXIF DateTimeDigitized"])
print (tags["EXIF ExifImageWidth"])
print (tags["EXIF ExifImageLength"])
print (tags["Image DateTime"])
#except:
props = os.stat(sDateinameUndPfad)
print("Größe des Objekts in Bytes:", props[6])
print("Zeitstempel des letzten Zugriffs auf das Objekt (atime):", props[7])
print("Zeitstempel der letzten Änderung des Objekts (mtime):", props[8])
print("Zeitstempel der letzten Änderung der Metadaten des Objekts (ctime):", props[9])





##   
##
##sDateinameUndPFad= sDateiname = sPruefsumme = "."
##
##walkVerzeichnis = "c:\\temp\\quelle\\"
###walkVerzeichnis = "I:\\000.Bilder.Sortiert"
###walkVerzeichnis = "C:\\01CM\\204_ProgrammiertesPython\\Testumgebung\\DateienNeu\\erledigt"
##
##
##
##aArray = []
##auslesenOrdnerRekursiv(walkVerzeichnis)
##
##conTemp.close()    
##


























