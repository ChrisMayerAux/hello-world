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
#   checkDateiInTempDBVorhanden
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def checkDateiInTempDBVorhanden(usPruefziffer):
    """
    die Funktion checkDateiInTempDBVorhanden liest den datensatz aus der TempDatenbank, der mit der übergebenen prüfsumme verknüpft ist.
    Übergabe: Prüfsumme
    Rückgabe: datensatz als Tuppel
    """

    MeinePfade = Class_lese_Config.Pfade()
    conTemp = sqlite3.connect(MeinePfade.tempdb)
    #print('funktion:   checkDateiInTempDBVorhanden --> daten: MeinePfade.tempdb',MeinePfade.tempdb)
    
    dbCursorTemp = conTemp.cursor()
    dbCursorTemp.execute("SELECT * FROM `Dateien` WHERE `Pruefsumme` LIKE '" + usPruefziffer + "'")  #"721482FF72B6F6642F6713CF01DB6BFC'")
    for datensatz in dbCursorTemp:
        return(datensatz)
  
