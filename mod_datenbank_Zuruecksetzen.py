#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
#import sys
#import exifread
import sqlite3


def datenbankZuruecksetzen(usTempDB):
    """
    die Funktion datenbankZuruecksetzen
        - Setzt die Temp datenbank zurück 
    Übergabe: usTempDB
    Rückgabe: --
    """
    filename = usTempDB
    os.remove(filename)

    #tabelle erstellen
    conTemp = sqlite3.connect(usTempDB)

    #tables erstellen
    dbcursor = conTemp.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `Dateien` (" \
          "`id` INTEGER PRIMARY KEY, " \
          "`UNCPfad` TEXT, " \
          "`Dateiname` TEXT, " \
          "`Pruefsumme` TEXT, " \
          "`DateinameNeu` TEXT)"

    dbcursor.execute(sql)
    conTemp.close()
