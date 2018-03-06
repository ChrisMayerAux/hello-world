#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time, locale
import sqlite3

#tabelle erstellen
conZiel = sqlite3.connect("datenbanken/dbZiel.db")

#tables erstellen
dbcursor = conZiel.cursor()
sql = "CREATE TABLE IF NOT EXISTS `Dateien` (" \
      "`id` INTEGER PRIMARY KEY, " \
      "`UNCPfad` TEXT, " \
      "`Dateiname` TEXT, " \
      "`Pruefsumme` TEXT, " \
      "`Eingabe1` TEXT, " \
      "`Eingabe2` TEXT, " \
      "`Eingabe3` TEXT, " \
      "`Eingabe4` TEXT)"
dbcursor.execute(sql)

#erste daten einfügen

personen = []
personen.append(["12", "23", "34"])


for person in personen:
    sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`) VALUES (" \
      "'" + person[0] + "', " \
      "'" + person[1] + "', " \
      "'" + person[2] + "')"
    dbcursor.execute(sql)
    conZiel.commit()
    print(dbcursor.lastrowid)  # gibt die ID des letzten Eintrags zurück

conZiel.close()

##########################################################
##########################################################
##########################################################
##########################################################


#tabelle erstellen
conTemp = sqlite3.connect("datenbanken/dbTemp.db")

#tables erstellen
dbcursor = conTemp.cursor()
sql = "CREATE TABLE IF NOT EXISTS `Dateien` (" \
      "`id` INTEGER PRIMARY KEY, " \
      "`UNCPfad` TEXT, " \
      "`Dateiname` TEXT, " \
      "`Pruefsumme` TEXT, " \
      "`Eingabe1` TEXT, " \
      "`Eingabe2` TEXT, " \
      "`Eingabe3` TEXT, " \
      "`Eingabe4` TEXT)"
dbcursor.execute(sql)

#erste daten einfügen

personen = []
personen.append(["12", "23", "34"])


for person in personen:
    sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`) VALUES (" \
      "'" + person[0] + "', " \
      "'" + person[1] + "', " \
      "'" + person[2] + "')"
    dbcursor.execute(sql)
    conTemp.commit()
    print(dbcursor.lastrowid)  # gibt die ID des letzten Eintrags zurück

conTemp.close()

