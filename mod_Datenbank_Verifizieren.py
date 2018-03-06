#!/usr/bin/python
# -*- coding: utf-8 -*-

from md5hash import scan
import os
import sys
import exifread
import sqlite3

import mod_Daten_zurueck_Geben
import mod_check_Datei_In_TempDB_Vorhanden

import Class_lese_Config



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   DatenbankVerifizieren Ende
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def DatenbankVerifizieren(usQuelle_Verzeichnis, usQuelle_Datenbank):
    """
    die Funktion DatenbankVerifizieren
        - kontrolliert alle datensätze ob eine entsprechende datei da ist - wenn nein - datensatz löschen!

    Übergabe: quelle_Dateien, quelle_Verzeichnis, quelle_Datenbank
    Rückgabe: -- möglicherweise mal ein ok ;)
                - später auf jeden fall mal ein logfile
    """    
    print('-------- DatenbankVerifizieren -------------------------------------------------------------------')

    #db ermitteln und füllen
    MeinePfade = Class_lese_Config.Pfade()

    ZaehlerGesamt = 0
    ZaehlerGeloescht = 0
    ZaehlerEingetragen = 0

    
    sQuellPfad = MeinePfade.quellpfad
    sZielpfad = MeinePfade.zielpfad
    sPfadZielDB = MeinePfade.zieldb
    sPfadTempDB = MeinePfade.tempdb

    if usQuelle_Verzeichnis == "quell":
        sQuelle_Verzeichnis = MeinePfade.quellpfad
    elif usQuelle_Verzeichnis == "ziel":
        sQuelle_Verzeichnis = MeinePfade.zielpfad
    else:
        #baustelle: test ob vorhanden und dann komplett raus?
        sQuelle_Verzeichnis = usQuelle_Verzeichnis

    if usQuelle_Datenbank == "temp":
        conDB = sqlite3.connect(sPfadTempDB)
        dbCursor = conDB.cursor()
    elif usQuelle_Datenbank == "ziel":
        conDB = sqlite3.connect(sPfadZielDB)
        dbCursor = conDB.cursor()
    #else:
        #baustelle: test ob vorhanden und dann komplett raus?        
    #    pass

##    print('funktion:    DatenbankVerifizieren --> daten: sQuellPfad: ', sQuellPfad)
##    print('funktion:    DatenbankVerifizieren --> daten: sZielpfad: ', sZielpfad)    
##    print('funktion:    DatenbankVerifizieren --> daten: sPfadZielDB: ', sPfadZielDB)
##    print('funktion:    DatenbankVerifizieren --> daten: sPfadTempDB: ', sPfadTempDB)
##    print('\n')
##    print('funktion:    DatenbankVerifizieren --> daten: sQuelle_Verzeichnis: ', sQuelle_Verzeichnis)
##    print('funktion:    DatenbankVerifizieren --> daten: dbCursor: ', dbCursor)
##    print('\n')

    #print('funktion:    DatenbankVerifizieren --> daten: usName_Datenbank: ', usName_Datenbank)   

    # daten holen
    # dbCursor.execute("SELECT * FROM `Dateien`")


    # Beispiel für eine Endlosschleife:
    y = 1
    x = 0

    while y != 0:
        #    print(x)
        #    x += 1
        Zaehler =+ 1
        y = 0
        #findet alle:
        dbCursor.execute("SELECT * FROM `Dateien`")

        for datensatz in dbCursor:
            #print('datensatz',     datensatz)
            sID = datensatz[0]
            sPfad = datensatz[1]
            sPruefsumme = datensatz[3]
            ZaehlerGesamt+=1
            #print('sID',     sID , '\n sPfad' , sPfad , '\n sPruefsumme' , sPruefsumme)

            if os.path.exists(sPfad) == True:
                b=20
                x+=1
                ZaehlerEingetragen = ZaehlerEingetragen +1
                #Zähler einbauen und alle 20 dateien eine meldung abgeben, dass es noch läuft wie es soll ...
                #if (x % b)== 0 :
                #    print('es wurden  ', x ,'  Datensätze verarbeitet')
                
            else:
                #print( sPfad + " existiert nicht.")
                #print ("++++", Zaehler)
                #print("DELETE FROM `Dateien` WHERE `ID` = '" + str(sID) + "'")
                sSQLAnweisung = "DELETE FROM `Dateien` WHERE `ID` = '" + str(sID) + "'"
                dbCursor.execute(sSQLAnweisung)
                conDB.commit()
                ZaehlerGeloescht+=1
                y = 1

    print('ZaehlerGesamt',     ZaehlerGesamt , '\nZaehlerGeloescht' , ZaehlerGeloescht , '\nZaehlerEingetragen' , ZaehlerEingetragen)
    print('-------- ende DatenbankVerifizieren --------------------------------------------------------------')
