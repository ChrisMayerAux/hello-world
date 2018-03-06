#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import exifread
from contextlib import suppress
import mod_ExifZeit_Umwandeln
import time, locale
from time import gmtime, strftime

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   ZielDBfuellen
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def ZielDBfuellen(walkVerzeichnis):
    """
    die Funktion ZielDBfuellen
        - arbeitet alle dateien im zielverzeichnis ab und schreibt die erhobenen daten in die ZielDatenbank.
        daten sind: UNCPfad, Dateiname, Pruefsumme, sDatenUndGroessen
    Übergabe: usTempDB
    Rückgabe: --
    """
    print('-------- ZielDBfuellen -------------------------------------------------------------------')
    for root, dirs, files in os.walk(walkVerzeichnis, topdown=False):
        for name in files:
            print('---------------------------------------------------------------------------')
            sDateinameUndPfad = os.path.join(root, name)
            sDateiname = (os.path.join(name))
            sPruefsumme = scan(sDateinameUndPfad)
            #sTest = DatenzurueckGeben('c:\\Temp\\ziel\\1.jpg')
            sDatenUndGroessen = DatenzurueckGeben(sDateinameUndPfad)
            print('funktion:    ZielDBfuellen --> daten: sDatenUndGroessen',sDatenUndGroessen)
            print('sDateinameUndPfad  :' + sDateinameUndPfad + '      und sDateiname  :' + sDateiname + '      und sPrüfsumme: ' + sPruefsumme)

            if checkDateiInZielDBVorhanden(sPruefsumme) == None:
                sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`, `DateinameNeu` ) VALUES (" \
                  "'" + sDateinameUndPfad + "', " \
                  "'" + sDateiname + "', " \
                  "'" + sPruefsumme + "', " \
                  "'" + sDatenUndGroessen + "')"
                
                print(sDatenUndGroessen)

                print('funktion:    ZielDBfuellen --> daten: sql', sql)
                dbCursorZiel.execute(sql)
                conZiel.commit()
                print('wurde unter dieser ID ' + str(dbCursorZiel.lastrowid) + ' in die DB aufgenommen eingepflegt')                               # gibt die ID des letzten Eintrags zurück
            else:
                print('datei is scho da')
                #Baustelle - Logging:
                # hier wäre ein log nicht schlecht, nur dass man weiß, wieviele dateien im quellordner dubletten sind.

    print('-------- ende ZielDBfuellen --------------------------------------------------------------')
