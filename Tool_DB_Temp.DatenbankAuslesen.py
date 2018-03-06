#!/usr/bin/python
# -*- coding: utf-8 -*-

from md5hash import scan
import os
import sys
import time, locale
import sqlite3

conTemp = sqlite3.connect("datenbanken/dbTemp.db")
dbCursor = conTemp.cursor()

#findet alle:
dbCursor.execute("SELECT * FROM `Dateien`")
for datensatz in dbCursor:
    print(datensatz)
conTemp.close()






