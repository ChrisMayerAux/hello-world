#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time, locale
import sqlite3

#tabelle erstellen
conZiel = sqlite3.connect("datenbanken/dbZiel.db")

dbcursor = conZiel.cursor()

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
