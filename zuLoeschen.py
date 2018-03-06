#!/usr/bin/python
# -*- coding: utf-8 -*-

from md5hash import scan
import os
import sys
import time, locale
import sqlite3
import shutil
from time import gmtime, strftime
import datetime
import exifread
from contextlib import suppress

import Class_lese_Config
import mod_Bilder_Bearbeiten
import mod_datenbank_Zuruecksetzen
import mod_Datenbank_fuellen
import mod_Datenbank_Verifizieren
import mod_Datenbank_Gegeneinander_Checken2

DateinameUndPFad= sDateiname = sPruefsumme = "."
sDateinameUndPFad= sDateiname = sPruefsumme = sDatensatz = "."

### pfade einlesen
MeinePfade = Class_lese_Config.Pfade()


###### baustelle:
####
###### hier werden die Dateien der ZielDB gecheckt - bei fehlenden dateien werden datensätze gelöscht
####mod_Datenbank_Verifizieren.DatenbankVerifizieren("ziel", "ziel")
####
####
###### hier noch füllen zieldb einfügen!
####mod_Datenbank_fuellen.DatenbankFuellen("ziel", "ziel")
####
####
###### teil zum einlesen der tempdatenbank:
###### alt: 
######mod_TempDB_fuellen.TempDBfuellen(sQuellPfad)
####mod_Datenbank_fuellen.DatenbankFuellen("quell", "temp")


## Datenbanken gegeneinander checken.
mod_Datenbank_Gegeneinander_Checken2.DatenbankCheck("ziel", "temp")
## mod_Datenbank_Gegeneinander_Checken("temp", "ziel")
