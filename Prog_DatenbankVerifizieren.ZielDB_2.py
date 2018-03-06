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


DateinameUndPFad= sDateiname = sPruefsumme = "."
sDateinameUndPFad= sDateiname = sPruefsumme = sDatensatz = "."

### pfade einlesen
MeinePfade = Class_lese_Config.Pfade()

## baustelle:
## hier noch kontrollieren ziel db einfügen
mod_Datenbank_Verifizieren.DatenbankVerifizieren("ziel", "ziel")

## hier noch füllen zieldb einfügen!
mod_Datenbank_fuellen.DatenbankFuellen("ziel", "ziel")

## Datenbanken gegeneinander checken.
mod_Datenbank_Gegeneinander_Checken.DatenbankCheck("ziel", "temp")
## mod_Datenbank_Gegeneinander_Checken("temp", "ziel")
