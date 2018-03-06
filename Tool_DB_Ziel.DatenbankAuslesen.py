#!/usr/bin/python
# -*- coding: utf-8 -*-

##from md5hash import scan
##import os
##import sys
##import time, locale
import sqlite3


def auslesen_Ziel_Datenbank():
    """ diese funktion liest alle daten aus der zieldatenbank aus und
        gibt sie auf der shell aus.
    """
    conZiel = sqlite3.connect("datenbanken/dbZiel.db")
    dbCursor = conZiel.cursor()

    #findet alle:
    dbCursor.execute("SELECT * FROM `Dateien`")
    for datensatz in dbCursor:
        print(datensatz)

    conZiel.close()


auslesen_Ziel_Datenbank()
