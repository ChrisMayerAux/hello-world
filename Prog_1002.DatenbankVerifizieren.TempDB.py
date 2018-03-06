#!/usr/bin/python
# -*- coding: utf-8 -*-

from md5hash import scan
import os
import sys
import time, locale
import sqlite3
from time import gmtime, strftime


#print(os.path.exists('I:\\000.Bilder.Sortiert\\2000.01\\2000.01.01.Handy.13.43.0.38.jpg'))

    

#now = time.time()
#sTest = str(strftime("%Y.%m.%d.%H.%M.%S" , time.localtime(time.time())))
print("Beginn: ", str(strftime("%Y.%m.%d.%H.%M.%S" , time.localtime(time.time()))))

conTemp = sqlite3.connect("datenbanken/dbTemp.db")
dbCursor = conTemp.cursor()


# Beispiel für eine Endlosschleife:
x = 1
while x > 0:
#    print(x)
#    x += 1
    x=0
    #findet alle:
    dbCursor.execute("SELECT * FROM `Dateien`")

    for datensatz in dbCursor:

        #print(datensatz)
        print ("++++++++++++++++++++++++++++++++")
        #print(datensatz[0])
        sID = datensatz[0]
        #print(" ID: " + str(sID))

        sPfad = datensatz[1]
        #print(" Pfad: " + str(sPfad))

        sPruefsumme = datensatz[3]
        #print(" Prüfsumme: " + str(sPruefsumme))    

        #print ("++++")
        
               
        if os.path.exists(sPfad) == True:
            print( sPfad + "   existiert.")
            #print ("++++")
            #x=1
            #Zähler einbauen
            
        else:
            print( sPfad + "   existiert nicht.")
            #print ("++++")
            print("DELETE FROM `Dateien` WHERE `ID` = '" + str(sID) + "'")
            print ("++++")
            sSQLAnweisung = "DELETE FROM `Dateien` WHERE `ID` = '" + str(sID) + "'"
            dbCursor.execute(sSQLAnweisung)
            conTemp.commit()
            x=1




conTemp.close()

print("Ende: ", str(strftime("%Y.%m.%d.%H.%M.%S" , time.localtime(time.time()))))

