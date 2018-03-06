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
import mod_Datenbank_Gegeneinander_Checken

DateinameUndPFad= sDateiname = sPruefsumme = "."
sDateinameUndPFad= sDateiname = sPruefsumme = sDatensatz = "."

### pfade einlesen
MeinePfade = Class_lese_Config.Pfade()


## um was checken zu können ...
mod_Datenbank_Verifizieren.DatenbankVerifizieren("ziel", "ziel")
mod_Datenbank_fuellen.DatenbankFuellen("ziel", "ziel")
mod_Datenbank_fuellen.DatenbankFuellen("quell", "temp")


## Datenbanken gegeneinander checken.
#mod_Datenbank_Gegeneinander_Checken.DatenbankCheck("ziel", "temp")
## mod_Datenbank_Gegeneinander_Checken("temp", "ziel")




## baustelle:


