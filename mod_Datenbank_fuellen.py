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



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   DatenbankFuellen Ende
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def DatenbankFuellen(usQuelle_Verzeichnis, usQuelle_Datenbank):
    """
    die Funktion DatenbankVerifizieren
        - kontrolliert alle datensätze ob eine entsprechende datei da ist - wenn nein - datensatz löschen!

    Übergabe: quelle_Dateien, quelle_Verzeichnis, quelle_Datenbank
    Rückgabe: -- möglicherweise mal ein ok ;)
                - später auf jeden fall mal ein logfile
    """    
    print('-------- DatenbankFuellen -------------------------------------------------------------------')

    #db ermitteln und füllen
    MeinePfade = Class_lese_Config.Pfade()
    
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

    print('funktion:    DatenbankFuellen --> daten: usQuelle_Verzeichnis: ', usQuelle_Verzeichnis)
    print('funktion:    DatenbankFuellen --> daten: sQuelle_Verzeichnis: ', sQuelle_Verzeichnis)    
    print('funktion:    DatenbankFuellen --> daten: usQuelle_Datenbank: ', usQuelle_Datenbank)
    print('\n')

    ZaehlerGesamtanzahl =0
    ZaehlerEingepflegt  =0
    ZaehlerBereitsVorhanden  =0
    ZaehlerDateiOhneSuchstring=0
    
    #print('funktion:    DatenbankFuellen --> daten: usQuelle_Datenbank: ', usQuelle_Datenbank)   
    # daten holen
    # dbCursor.execute("SELECT * FROM `Dateien`")
   
    for root, dirs, files in os.walk(sQuelle_Verzeichnis, topdown=False):
        for name in files:
            #print('---------------------------------------------------------------------------')
            sDateinameUndPfad = os.path.join(root, name)
            sDateiname = (os.path.join(name))
            sPruefsumme = scan(sDateinameUndPfad)

            ZaehlerGesamtanzahl += 1
            #print('funktion:    DatenbankFuellen -->\n      sDateinameUndPfad  :' + sDateinameUndPfad + '\n      und sDateiname  :' + sDateiname + '\n      und sPrüfsumme: ' + sPruefsumme)

            #Hier werden die suchstrings definidert .... sollte noch was nötig sein ...
            sSuchString = (".jp", ".avi",  ".mp", ".png", ".JP", ".AVI",  ".MP", ".PNG")
            bVorhandenTrue = False

            for sSuchstrings in sSuchString:
                if sDateiname.find(sSuchstrings) != -1:
                    bVorhandenTrue = True

            if bVorhandenTrue == True:
                    
                #print('!!funktion:    DatenbankFuellen --> daten: sDateinameUndPfad',sDateinameUndPfad)
                sDatenUndGroessen = mod_Daten_zurueck_Geben.DatenzurueckGeben(sDateinameUndPfad)
                #print('!!funktion:    DatenbankFuellen --> daten: sDatenUndGroessen',sDatenUndGroessen)
                
                #print('sDateinameUndPfad  :' + sDateinameUndPfad + '      und sDateiname  :' + sDateiname + '      und sPrüfsumme: ' + sPruefsumme)


                bMerker = False
                if usQuelle_Verzeichnis == "ziel":
                    if mod_check_Datei_In_ZielDB_Vorhanden.checkDateiInZielDBVorhanden(sPruefsumme) == None:
                        bMerker = True
                        #print('in mod_check_Datei_In_ZielDB_Vorhanden')
                else:
                    if mod_check_Datei_In_TempDB_Vorhanden.checkDateiInTempDBVorhanden(sPruefsumme) == None:
                        bMerker = True
                        #print('in mod_check_Datei_In_TempDB_Vorhanden')

                if bMerker == True:
                    sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`, `DateinameNeu` ) VALUES (" \
                      "'" + sDateinameUndPfad + "', " \
                      "'" + sDateiname + "', " \
                      "'" + sPruefsumme + "', " \
                      "'" + sDatenUndGroessen + "')"
                    
                    #print(sDatenUndGroessen)
                    #print('funktion:    TempDBfuellen --> daten: sql', sql)

                    dbCursor.execute(sql)
                    conDB.commit()
                    #print('wurde unter dieser ID ' + str(dbCursor.lastrowid) + ' in die DB ' + usQuelle_Datenbank + ' aufgenommen eingepflegt')                               # gibt die ID des letzten Eintrags zurück
                    ZaehlerEingepflegt+=1

                else:
                    ZaehlerBereitsVorhanden+=1
                    #print('datei is scho da')
                    #Baustelle - Logging:
                    # hier wäre ein log nicht schlecht, nur dass man weiß, wieviele dateien im quellordner dubletten sind.

            else:
                ZaehlerDateiOhneSuchstring+=1
                #print("suchstring nicht vorhanden")

    print('\n ZaehlerGesamtanzahl ' , ZaehlerGesamtanzahl , '\n ZaehlerEingepflegt ' , ZaehlerEingepflegt , '\n ZaehlerBereitsVorhanden ' , ZaehlerBereitsVorhanden , '\n ZaehlerDateiOhneSuchstring ' , ZaehlerDateiOhneSuchstring)
    print('-------- ende DatenbankFuellen --------------------------------------------------------------')
