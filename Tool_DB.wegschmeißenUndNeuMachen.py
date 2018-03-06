#!/usr/bin/python
# -*- coding: utf-8 -*-

#* String			UNCPfad						\\192.168.177.210\Bilder\2016.05\2016.05.10.13.55.55.254.jpg
#* String			Dateiname					2016.05.10.13.55.55.254.jpg
#* String			Prüfsumme					5dfs186sdf186we5f13sdf


import os
import time, locale
import sqlite3

#erst die beiden datenbanken löschen:

filename = "datenbanken/dbZiel.db"
os.remove(filename)

filename = "datenbanken/dbTemp.db"
os.remove(filename)


#tabelle erstellen
conZiel = sqlite3.connect("datenbanken/dbZiel.db")
conTemp = sqlite3.connect("datenbanken/dbTemp.db")
dbTempCursor = conTemp.cursor()
dbZielCursor = conZiel.cursor()

sql = "CREATE TABLE IF NOT EXISTS `Dateien` (" \
      "`id` INTEGER PRIMARY KEY, " \
      "`UNCPfad` TEXT, " \
      "`Dateiname` TEXT, " \
      "`Pruefsumme` TEXT, " \
      "`DateinameNeu` TEXT)"

dbTempCursor.execute(sql)
dbZielCursor.execute(sql)

conTemp.close()
conZiel.close()
