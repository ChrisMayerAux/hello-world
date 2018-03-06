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


sDateinameUndPFad= sDateiname = sPruefsumme = "."

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#   ExifZeitUmwandeln
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ExifZeitUmwandeln(UeberGabeString):
    #von dateityp 'exifread.classes.IfdTag' nach string umwandeln
    sDatumZeit = str(UeberGabeString)

    #wenn hier nix drin is:
    if len(sDatumZeit) <=1:
        sDatumZeit = "2032.01.01.11.11.11"

    #umwandeln der eventuell kommenden zeichen nach punkt
    sDatumZeit = sDatumZeit.replace(':', '.')
    sDatumZeit = sDatumZeit.replace(' ', '.')
    sDatumZeit = sDatumZeit.replace('-', '.')

    return  sDatumZeit
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#   ExifZeitUmwandeln Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#   DateiZeitUmwandeln
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def DateiZeitUmwandeln(UeberGabeString):
    return  strftime("%Y.%m.%d.%H.%M.%S" ,time.localtime(UeberGabeString))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#   DateiZeitUmwandeln Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#   DatenzurueckGeben
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def DatenzurueckGeben(usDateinameUndPfad):
    sDateinameUndPfad = usDateinameUndPfad
    # datei öffnen für exif read
    f = open(sDateinameUndPfad, 'rb')
    #und lesen
    tags = exifread.process_file(f)

    # und wenn es keinen tag gibt
    sDatumZeitOrginalEpoch= sDatumZeitDigitalisiertEpoch = sDatumZeitBildEpoch = sDatumZeitDateiatime = sDatumZeitDateimtime = sDatumZeitDateictime =  2082708671                     #datum auf 2038 gestellt ...
    sBildbreite = sBildhoehe = 0
    print(' -- DatenzurueckGeben(usDateinameUndPfad): -- ', usDateinameUndPfad)

    with suppress(KeyError):

        #exif zeug lesen und zeiten umwandeln
        sDatumZeitOrginal = ExifZeitUmwandeln((tags["EXIF DateTimeOriginal"]))
        pattern = '%Y.%m.%d.%H.%M.%S'
        sDatumZeitOrginalEpoch = int(time.mktime(time.strptime(sDatumZeitOrginal, pattern)))
        sDatumZeitDigitalisiert = ExifZeitUmwandeln((tags["EXIF DateTimeDigitized"]))
        sDatumZeitDigitalisiertEpoch = int(time.mktime(time.strptime(sDatumZeitDigitalisiert, pattern)))
        sDatumZeitBild = ExifZeitUmwandeln((tags["Image DateTime"]))
        sDatumZeitBildEpoch = int(time.mktime(time.strptime(sDatumZeitBild, pattern)))
        sBildbreite = ExifZeitUmwandeln((tags["EXIF ExifImageWidth"]))
        sBildhoehe = ExifZeitUmwandeln((tags["EXIF ExifImageLength"]))

    #dateizeug lesen und umwandeln
    props = os.stat(sDateinameUndPfad)

    #baustelle: sollte die größe des objekts nötig sein ...
    #print("Größe des Objekts in Bytes:", props[6])

    sDatumZeitDateiatime = props[7]
    sDatumZeitDateimtime = props[8]
    sDatumZeitDateictime = props[9]

    #auswerten udn ältestes datum zurückgeben
    if sDatumZeitOrginalEpoch > sDatumZeitDigitalisiertEpoch:
                sEndDatum = sDatumZeitDigitalisiertEpoch
    else:
                sEndDatum = sDatumZeitOrginalEpoch

    if sEndDatum > sDatumZeitBildEpoch:
                sEndDatum = sDatumZeitBildEpoch

    if sEndDatum > sDatumZeitDateiatime:
                sEndDatum = sDatumZeitDateiatime

    if sEndDatum > sDatumZeitDateimtime:
                sEndDatum = sDatumZeitDateimtime

    if sEndDatum > sDatumZeitDateictime:
                sEndDatum = sDatumZeitDateictime

    #rückgabearray zusammenbasteln
    a = str(strftime("%Y.%m.%d.%H.%M.%S" , time.localtime(sEndDatum)))
    return a
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#   DatenzurueckGeben Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



def checkDateiVorhanden(usPruefziffer):
    dbCursor = conZiel.cursor()
    dbCursor.execute("SELECT * FROM `Dateien` WHERE `Pruefsumme` LIKE '" + usPruefziffer + "'")  #"721482FF72B6F6642F6713CF01DB6BFC'")
    for datensatz in dbCursor:
        return(datensatz)
    

def auslesenOrdnerRekursiv(walk_dir):
    for root, dirs, files in os.walk(walk_dir, topdown=False):
        for name in files:
            sDateinameUndPfad = os.path.join(root, name)
            sDateiname = (os.path.join(name))
            sPruefsumme = scan(sDateinameUndPfad)
            #sTest = modul_709_AEltestesDatum_Datei.DatenzurueckGeben('c:\\temp\\ziel\\1.jpg')

            sDatenUndGroessen = DatenzurueckGeben(sDateinameUndPfad)
            print(sDatenUndGroessen)

            if checkDateiVorhanden(sPruefsumme) == None:
                sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`, `DateinameNeu` ) VALUES (" \
                  "'" + sDateinameUndPfad + "', " \
                  "'" + sDateiname + "', " \
                  "'" + sPruefsumme + "', " \
                  "'" + sDatenUndGroessen + "')"

                print(sql)
                
                dbCursor.execute(sql)
                conZiel.commit()
                print('wurde unter dieser ID' + str(dbCursor.lastrowid) + ' in die DB aufgenommen eingepflegt')                               # gibt die ID des letzten Eintrags zurück
            else:
                print('datei is scho da')
                #hier muss ein "schon vorhanden fac gesetzt werden, also alles nochmal auslesen + das flac
####                
####                sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`, `DateinameNeu`, `Datum1`, `Datum2`, `Datum3`, `Datum4`, `Datum5`, `Datum6`, `BildBreite`, `BildLaenge`, `Dublette` ) VALUES (" \
####                  "'" + sDateinameUndPfad + "', " \
####                  "'" + sDateiname + "', " \
####                  "'" + sPruefsumme + "', " \
####
####                for inhalt in sDatenUndGroessen:
####                    sql = sql + "'" + str(inhalt) + "', "
####
####                sql = sql + "'Dublette')"
####                
####
####                print(sql)
####                
####                dbCursor.execute(sql)
####                conZiel.commit()
####                print('wurde unter dieser ID' + str(dbCursor.lastrowid) + ' in die DB aufgenommen eingepflegt')                               # gibt die ID des letzten Eintrags zurück



                

#walkVerzeichnis = "C:\\01CM\\204_ProgrammiertesPython\\Testumgebung\\ziel"
walkVerzeichnis = "c:\\temp\\ziel\\"

#tabelle erstellen
conZiel = sqlite3.connect("datenbanken/dbZiel.db")
dbCursor = conZiel.cursor()
aArray = []
auslesenOrdnerRekursiv(walkVerzeichnis)

conZiel.close()                                                         #datenbankverbindung zumachen








