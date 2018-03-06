#!/usr/bin/python
# -*- coding: utf-8 -*-

from md5hash import scan
import os
import sys
import exifread

import mod_Daten_zurueck_Geben
import mod_check_Datei_In_TempDB_Vorhanden

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   TempDBfuellen Ende
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def TempDBfuellen(walkVerzeichnis):
    """
    die Funktion TempDBfuellen
        - arbeitet alle dateien im zielverzeichnis ab und schreibt die erhobenen daten in die TempDatenbank.
        daten sind: UNCPfad, Dateiname, Pruefsumme, sDatenUndGroessen
    Übergabe: usTempDB
    Rückgabe: --
    """    
    print('-------- TempDBfuellen -------------------------------------------------------------------')
    for root, dirs, files in os.walk(walkVerzeichnis, topdown=False):
        for name in files:
            #print('---------------------------------------------------------------------------')
            sDateinameUndPfad = os.path.join(root, name)
            sDateiname = (os.path.join(name))
            sPruefsumme = scan(sDateinameUndPfad)
            #sTest = DatenzurueckGeben('c:\\temp\\ziel\\1.jpg')

            #sDateiname = "2012-05-18 11.23.50.jpg"
            #Hier werden die suchstrings definidert .... sollte noch was nötig sein ...

            sSuchString = (".jp", ".avi",  ".mp", )

            bVorhandenTrue = False

            for sSuchstrings in sSuchString:
                if sDateiname.find(sSuchstrings) != -1:
                    bVorhandenTrue = True

            if bVorhandenTrue == True:
                    
                sDatenUndGroessen = mod_Daten_zurueck_Geben.DatenzurueckGeben(sDateinameUndPfad)
                #print('funktion:    TempDBfuellen --> daten: sDatenUndGroessen',sDatenUndGroessen)
                #print('sDateinameUndPfad  :' + sDateinameUndPfad + '      und sDateiname  :' + sDateiname + '      und sPrüfsumme: ' + sPruefsumme)

                if mod_check_Datei_In_TempDB_Vorhanden.checkDateiInTempDBVorhanden(sPruefsumme) == None:
                    sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`, `DateinameNeu` ) VALUES (" \
                      "'" + sDateinameUndPfad + "', " \
                      "'" + sDateiname + "', " \
                      "'" + sPruefsumme + "', " \
                      "'" + sDatenUndGroessen + "')"
                    
                    #print(sDatenUndGroessen)

                    #print('funktion:    TempDBfuellen --> daten: sql', sql)

                    dbCursorTemp.execute(sql)
                    conTemp.commit()
                    print('wurde unter dieser ID ' + str(dbCursorTemp.lastrowid) + ' in die DB aufgenommen eingepflegt')                               # gibt die ID des letzten Eintrags zurück
                else:
                    print('datei is scho da')
                    #Baustelle - Logging:
                    # hier wäre ein log nicht schlecht, nur dass man weiß, wieviele dateien im quellordner dubletten sind.

            else:
                print("nicht vorhanden")

    print('-------- ende TempDBfuellen --------------------------------------------------------------')
