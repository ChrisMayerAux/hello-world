#!/usr/bin/python
# -*- coding: utf-8 -*-

from md5hash import scan
import os
import sys
import time, locale
import sqlite3



#print(os.path.exists('I:\\000.Bilder.Sortiert\\2000.01\\2000.01.01.Handy.13.43.0.38.jpg'))






conZiel = sqlite3.connect("datenbanken/dbZiel.db")
dbCursor = conZiel.cursor()


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
            conZiel.commit()
            x=1




conZiel.close()


