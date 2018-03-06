#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time, locale
import shutil

sQuellPfad = "c:\\temp\\Quelle\\"
sZielPfad = "c:\\temp\\Ziel\\"

sDateiname = "."

def ErstelleZeitstempel(usDateiMitPFad): 
    # -> hol den zeitstempel der datei -> creation
    timestamp = (os.path.getmtime(usDateiMitPFad))
    datetime = time.localtime(timestamp)

    # --> hier die 
    sTag = (time.strftime("%d", datetime))
    sMonat = (time.strftime("%m", datetime))
    sJahr = (time.strftime("%Y", datetime))
    sStunde = (time.strftime("%H", datetime))
    sMinute = (time.strftime("%M", datetime))
    sSekunde = (time.strftime("%S", datetime))

    return  sJahr + "_" + sMonat + "_" + sTag + "_" + sStunde + "_" + sMinute + "_" + sSekunde  


sQuelleDateiMitPfad = sQuellPfad + 'quelle.jpg'

file = ('c:\\temp\\quelle\\quelle.jpg')
sDateiname = (ErstelleZeitstempel(file)+ '.jpg')

print(sDateiname)

sZielDateiMitPfad = sZielPfad + sDateiname

print("++++++++++++++++++++++++++++++++")
print(sQuelleDateiMitPfad)
print(sZielDateiMitPfad)
print("++++++++++++++++++++++++++++++++")


if sDateiname == "":
    print("dateiname leer")
else:
    print("umbenennung")
    shutil.copy2(sQuelleDateiMitPfad, sZielDateiMitPfad)


################## kopieren
#source = os.environ['HOME'] + "/Python/testdatei"
#target = os.environ['HOME'] + "/Python/testdatei2"
#shutil.copy2(sQuelleDateiMitPfad, target)
############################

#ausgabe der verschiedenen Daten als Tue May 18 09:23:03 2010
#import os.path, time
#print ("mtime: %s" % time.ctime(os.path.getmtime(file)))
#print ("ctime: %s" % time.ctime(os.path.getctime(file)))
#print ("atime: %s" % time.ctime(os.path.getatime(file)))


#print ("**********************************************************")
# ausgabe des datums des files
#sDatum =(time.ctime(os.path.getatime(file)))
#print (sDatum)
#p#rint ("**********************************************************")

#print ("**********************************************************")
# ausgabe des datums des files
#timestamp = time.mktime((now))
#print (timestamp)
#print ("**********************************************************")
#print ("**********************************************************")
#print ("**********************************************************")
#print ("**********************************************************")


#Strings deklarieren
#strJahr = strMonat = strOrdnername = "."

# zeit auslesen
#now = time.localtime()

#Jahr und Monat auslesen
#strJahr = str(now.tm_year)
#strMonat = str(now.tm_mon)

# ordnernamen zusammenbauen
#strOrdnername = strJahr + "." + strMonat

# ausgabe des ornernamens
#print ("der ordnername: ", strOrdnername)

#sQuellPfad = "c:\\temp\\Quelle\\"
#sZielPfad = "c:\\temp\\Ziel\\"
#print('kopiert wird von: \n -->   ' + sQuellPfad + "   \n nach \n -->   "  + sZielPfad + '\n')

#file = ('c:\\temp\\quelle\\quelle.jpg')
#statinfo = os.stat('C:\\01CM\\400 CM\\001_BAU\\01_Pläne\\2012_10_28\\1OG.jpg')
#print (statinfo)


