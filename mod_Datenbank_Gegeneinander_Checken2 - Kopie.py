#!/usr/bin/python
# -*- coding: utf-8 -*-

from md5hash import scan
import os
import sys
import exifread
import sqlite3

import mod_Daten_zurueck_Geben
import mod_check_Datei_In_TempDB_Vorhanden
import mod_check_Datei_In_ZielDB_Vorhanden

import Class_lese_Config



import time, locale
from time import gmtime, strftime






#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   DatenbankCheck Ende
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def DatenbankCheck(usDB1, usDB2):
    """
    die Funktion DatenbankCheck
        - Alle Datensätze aus Temp die in Ziel Vorkommen in Temp löschen.
          wobei db1 die ZielDB ist
          und   db2 die TempDB
          
        ich überleg noch ob ich die funktion andersrum auch mal brauchen kann ... ;)
    """    
    print('-------- DatenbankCheck -------------------------------------------------------------------')
    print("Beginn: ", str(strftime("%Y.%m.%d.%H.%M.%S" , time.localtime(time.time()))))

    #db ermitteln und füllen
    MeinePfade = Class_lese_Config.Pfade()
    
    sQuellPfad = MeinePfade.quellpfad
    sZielpfad = MeinePfade.zielpfad
    sPfadZielDB = MeinePfade.zieldb
    sPfadTempDB = MeinePfade.tempdb

    #if usQuelle_Verzeichnis == "quell":
    sDB1 = sPfadZielDB
    #elif usQuelle_Verzeichnis == "ziel":
    sDB2 = sPfadTempDB

    print('funktion:    DatenbankCheck --> daten: sQuellPfad: ', sQuellPfad)
    print('funktion:    DatenbankCheck --> daten: sZielpfad: ', sZielpfad)
    print('funktion:    DatenbankCheck --> daten: sDB1: ', sDB1)    
    print('funktion:    DatenbankCheck --> daten: sDB2: ', sDB2)

    ZaehlerGesamtanzahl = 0
    ZaehlerGeloescht = 0
    ZaehlerBereitsVorhanden = 0
    ZaehlerDateiOhneSuchstring = 0
    b=1000

    #else:
    #baustelle: test ob vorhanden und dann komplett raus?
    #sQuelle_Verzeichnis = usQuelle_Verzeichnis
    ## datenbanken zuordnern und verbinden
    
    conDB1 = sqlite3.connect(sDB1)
    db1Cursor = conDB1.cursor()
    conDB2 = sqlite3.connect(sDB2)
    db2Cursor = conDB2.cursor()
        

    # Beispiel für eine Endlosschleife:
    y = 1
    x = 0

    db2Cursor.execute("SELECT * FROM `Dateien`")        #Temp

      
    for datensatzTemp in db2Cursor:
        sIDTemp = datensatzTemp[0]
        sPfadTemp = datensatzTemp[1]
        sPruefsummeTemp = datensatzTemp[3]
        #print ("++++" , sIDTemp , "++++" , sPfadTemp , "++++" , sPruefsummeTemp , "++++")
        ZaehlerGesamtanzahl+=1

        #dbCursorZiel = conZiel.cursor()
        #db1Cursor.execute("SELECT * FROM `Dateien` WHERE `Pruefsumme` LIKE '" + sPruefsummeTemp + "'")  #"721482FF72B6F6642F6713CF01DB6BFC'")

        while y != 0:
            #    print(x)
            #    x += 1
            y = 0
            #findet alle:

            bMerker = False
            if mod_check_Datei_In_ZielDB_Vorhanden.checkDateiInZielDBVorhanden(sPruefsummeTemp) == None:
                bMerker = True
                print('in mod_check_Datei_In_ZielDB_Vorhanden  ' , sIDTemp)

            #for datensatzZiel in db1Cursor:
                #return(datensatz)

            if bMerker == True:
                #x+=1
                ZaehlerBereitsVorhanden+=1
                #Zähler einbauen und alle 20 dateien eine meldung abgeben, dass es noch läuft wie es soll ...
                if (ZaehlerBereitsVorhanden % b)== 0 :
                    print('es wurden  ', ZaehlerBereitsVorhanden ,'  Datensätze verarbeitet')
                    y = 1
                
            else:
                #sIDZiel = datensatzZiel[0]
                #sPfadZiel = datensatzZiel[1]
                #sPruefsummeZiel = datensatzZiel[3]
                ZaehlerGeloescht+=1
                print ("++++")
                print("DELETE FROM `Dateien` WHERE `ID` = '" + str(sIDTemp) + "'")
                sSQLAnweisung = "DELETE FROM `Dateien` WHERE `ID` = '" + str(sIDTemp) + "'"
                db2Cursor.execute(sSQLAnweisung)
                conDB2.commit()
                y = 1
                bMerker = False

    
    print('\n ZaehlerGesamtanzahl ' , ZaehlerGesamtanzahl , '\n ZaehlerBereitsVorhanden ' , ZaehlerBereitsVorhanden , '\n ZaehlerGeloescht ' , ZaehlerGeloescht , '\n ZaehlerDateiOhneSuchstring ' , ZaehlerDateiOhneSuchstring)
    print("Beginn: ", str(strftime("%Y.%m.%d.%H.%M.%S" , time.localtime(time.time()))))
    print('-------- ende DatenbankCheck --------------------------------------------------------------')
