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


## baustelle:

## hier werden die Dateien der ZielDB gecheckt - bei fehlenden dateien werden datensätze gelöscht
mod_Datenbank_Verifizieren.DatenbankVerifizieren("ziel", "ziel")


## hier noch füllen zieldb einfügen!
mod_Datenbank_fuellen.DatenbankFuellen("ziel", "ziel")


## teil zum einlesen der tempdatenbank:
## alt: 
##mod_TempDB_fuellen.TempDBfuellen(sQuellPfad)
mod_Datenbank_fuellen.DatenbankFuellen("quell", "temp")

## Datenbanken gegeneinander checken.
mod_Datenbank_Gegeneinander_Checken.DatenbankCheck("ziel", "temp")
## mod_Datenbank_Gegeneinander_Checken("temp", "ziel")


## teil zum kopieren der Bilder
mod_Bilder_Bearbeiten.BilderBearbeiten()



##print('------------- modul_ZielDBinit.auslesenOrdnerRekursiv --------------------------------------------------------------')
## alt:
##mod_ZielDB_fuellen.ZielDBfuellen(sZielpfad)
mod_Datenbank_fuellen.DatenbankFuellen("ziel", "ziel")
##print('-------- ende modul_ZielDBinit.auslesenOrdnerRekursiv --------------------------------------------------------------')

##conTemp.close()
##conZiel.close()

mod_datenbank_Zuruecksetzen.datenbankZuruecksetzen(MeinePfade.tempdb)





#####Datenbanken verbinden:
####conTemp = sqlite3.connect(sPfadTempDB)
####dbCursorTemp = conTemp.cursor()
####
####conZiel = sqlite3.connect(sPfadZielDB)
####dbCursorZiel = conZiel.cursor()

##
##sQuellPfad = MeinePfade.quellpfad
##sZielpfad = MeinePfade.zielpfad
##sPfadZielDB = MeinePfade.zieldb
##sPfadTempDB = MeinePfade.tempdb
##


#sPfad = "c:\\temp\\quelle\\"
#sQuellPfad = "C:\\01CM\\400 CM\\003_HandyBilder\\"
#sQuellPfad = "C:\\Temp\\quelle\\fehler1\\"
#sQuellPfad = "c:\\temp\\testumgebung\\"
#sQuellPfad = "C:\\01CM\\930 bilder\\LSV_2004_richie"
#sQuellPfad = "C:\\01CM\\930 bilder\\LSV_2004_richie"
#sQuellPfad = "I:\\000.Bilder.Sortiert"
#sQuellPfad = "C:\\01CM\\204_ProgrammiertesPython\\Testumgebung\\DateienNeu\\erledigt"

