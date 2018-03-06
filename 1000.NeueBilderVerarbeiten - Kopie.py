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


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   checkDateiInZielDBVorhanden
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def checkDateiInZielDBVorhanden(usPruefziffer):
    dbCursorZiel = conZiel.cursor()
    dbCursorZiel.execute("SELECT * FROM `Dateien` WHERE `Pruefsumme` LIKE '" + usPruefziffer + "'")  #"721482FF72B6F6642F6713CF01DB6BFC'")
    for datensatz in dbCursorZiel:
        print('funktion:    checkDateiInZielDBVorhanden --> daten: datensatz: ', datensatz[0])
        print('funktion:    checkDateiInZielDBVorhanden --> daten: type(datensatz): ', type(datensatz))        
        return(datensatz)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   checkDateiInZielDBVorhanden Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   checkDateiInTempDBVorhanden
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def checkDateiInTempDBVorhanden(usPruefziffer):
    dbCursorTemp = conTemp.cursor()
    dbCursorTemp.execute("SELECT * FROM `Dateien` WHERE `Pruefsumme` LIKE '" + usPruefziffer + "'")  #"721482FF72B6F6642F6713CF01DB6BFC'")
    for datensatz in dbCursorTemp:
        return(datensatz)
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   checkDateiInTempDBVorhanden Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  

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
    print('funktion:    DatenzurueckGeben --> daten: sDateinameUndPfad',sDateinameUndPfad)
    
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


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   datenbankZuruecksetzen
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def datenbankZuruecksetzen(usTempDB):
    filename = usTempDB
    os.remove(filename)

    #tabelle erstellen
    conTemp = sqlite3.connect(usTempDB)

    #tables erstellen
    dbcursor = conTemp.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `Dateien` (" \
          "`id` INTEGER PRIMARY KEY, " \
          "`UNCPfad` TEXT, " \
          "`Dateiname` TEXT, " \
          "`Pruefsumme` TEXT, " \
          "`DateinameNeu` TEXT)"

    dbcursor.execute(sql)

    #erste daten einfügen
    datenArray = []
    datenArray.append(["12", "23", "34"])

    for Datum in datenArray:
        sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`) VALUES (" \
          "'" + Datum[0] + "', " \
          "'" + Datum[1] + "', " \
          "'" + Datum[2] + "')"
        
        dbcursor.execute(sql)
        conTemp.commit()
        print('Datenbank zurückgesetzt --> ', usTempDB ,  '! Letzte ID: ', dbcursor.lastrowid)  # gibt die ID des letzten Eintrags zurück

    conTemp.close()
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   datenbankZuruecksetzen Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   BilderBearbeiten
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def BilderBearbeiten():
    print('------------- BilderBearbeiten --------------------------------------------------------------')
    dbCursorTemp.execute("SELECT * FROM `Dateien`")                 #Findet nimmt alle daten aus der datenbank Temp
    for datensatz in dbCursorTemp:                                  #und arbeitet sie ab
        #print(datensatz[3])                                         #gibt die Prüfsumme aus
        print('funktion:    BilderBearbeiten --> daten: datensatz[3](Prüfsumme): ',datensatz[3])
        sID = checkDateiInZielDBVorhanden(datensatz[3])             #Übergibt die prüfsumme an PruefsummeInZielVorhanden bekommt ID zurück

        #print('funktion:    BilderBearbeiten --> daten: sID: ', sID[0])
        #print('funktion:    BilderBearbeiten --> daten: type(sID): ', type(sID[0]))
        
        #dann kann ich mal schauen, ob des dann tatsächlich auch so abgeprüft werden kann ...

##--> das ist der aufruf in db füllen ... mal sehen ob der funktioniert ohne die ganzen luftsprünge ...

##        if sID != 0:
        
        ##print('funktion:    BilderBearbeiten --> daten: sPruefsumme: ',sPruefsumme)
        ##print('funktion:    BilderBearbeiten --> daten: checkDateiInZielDBVorhanden(sPruefsumme): ',checkDateiInZielDBVorhanden(sPruefsumme))
        
        if checkDateiInZielDBVorhanden(sPruefsumme) != None:


            #Datei bereits vorhanden.
            print("Datei bereits vorhanden" + str(sID))
            print('funktion:    BilderBearbeiten --> daten: sID: ', datensatz)
            #bDBZielNeuEinlesen = True
            
####        elif sID == None:
####            #Datei bereits vorhanden.
####            print("Datei bereits vorhanden" + str(sID))
####            print('funktion:    BilderBearbeiten --> daten: sID: ', datensatz)
####            #bDBZielNeuEinlesen = True
        
        else:
##            hier müssen die entspechenden daten kopiert werden
            print('funktion:    BilderBearbeiten --> daten: sID: ', sID)
            print("daten kopieren")
            print('funktion:    BilderBearbeiten --> daten: sID: ', datensatz[2])

##            prüfen ob ordner in zielstruktur vorhanden?                       - läuft
            sPfad = sZielpfad + (datensatz[4][:7])

            if os.path.exists(sPfad) == True:
                print(sPfad, "existiert.")
            else:
                print(sPfad, "existiert nicht.")
                os.mkdir(sPfad)

##            datei umbenennen und kopieren
            sQuellPfadUndDatei = datensatz[1]
            sZielPfadUndDatei = sPfad + '\\' + datensatz[4] + ("." + datensatz[2] [len(datensatz[2])-4:]).replace("..",".")

##            print('sQuellPfadUndDatei ' + sQuellPfadUndDatei)
            print('funktion:    BilderBearbeiten --> daten: sQuellPfadUndDatei: ', sQuellPfadUndDatei) 
            # bedeutet: punkt und die letzten 4 des dateinamens, replaced werden 2 gegen einen punkt
            #print(("." + datensatz[2] [len(datensatz[2])-4:]).replace("..","."))
##            print('sZielPfadUndDatei ' + sZielPfadUndDatei)
            print('funktion:    BilderBearbeiten --> daten: sZielPfadUndDatei: ', sZielPfadUndDatei) 

            try:
                shutil.copy2(sQuellPfadUndDatei, sZielPfadUndDatei)

            except(FileNotFoundError):
                pass

    print('-------- ende BilderBearbeiten --------------------------------------------------------------')
            
##            datei schrumpfen
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   BilderBearbeiten Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   ZielDBfuellen
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def ZielDBfuellen(walkVerzeichnis):
    print('-------- ZielDBfuellen -------------------------------------------------------------------')
    for root, dirs, files in os.walk(walkVerzeichnis, topdown=False):
        for name in files:
            print('---------------------------------------------------------------------------')
            sDateinameUndPfad = os.path.join(root, name)
            sDateiname = (os.path.join(name))
            sPruefsumme = scan(sDateinameUndPfad)
            #sTest = DatenzurueckGeben('c:\\Temp\\ziel\\1.jpg')
            sDatenUndGroessen = DatenzurueckGeben(sDateinameUndPfad)
            print('funktion:    ZielDBfuellen --> daten: sDatenUndGroessen',sDatenUndGroessen)
            print('sDateinameUndPfad  :' + sDateinameUndPfad + '      und sDateiname  :' + sDateiname + '      und sPrüfsumme: ' + sPruefsumme)

            if checkDateiInZielDBVorhanden(sPruefsumme) == None:
                sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`, `DateinameNeu` ) VALUES (" \
                  "'" + sDateinameUndPfad + "', " \
                  "'" + sDateiname + "', " \
                  "'" + sPruefsumme + "', " \
                  "'" + sDatenUndGroessen + "')"
                
                print(sDatenUndGroessen)

                print('funktion:    ZielDBfuellen --> daten: sql', sql)

                dbCursorZiel.execute(sql)
                conZiel.commit()
                print('wurde unter dieser ID ' + str(dbCursorZiel.lastrowid) + ' in die DB aufgenommen eingepflegt')                               # gibt die ID des letzten Eintrags zurück
            else:
                print('datei is scho da')
                #Baustelle - Logging:
                # hier wäre ein log nicht schlecht, nur dass man weiß, wieviele dateien im quellordner dubletten sind.

    print('-------- ende ZielDBfuellen --------------------------------------------------------------')
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   ZielDBfuellen Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   TempDBfuellen
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def TempDBfuellen(walkVerzeichnis):
    print('-------- TempDBfuellen -------------------------------------------------------------------')
    for root, dirs, files in os.walk(walkVerzeichnis, topdown=False):
        for name in files:
            print('---------------------------------------------------------------------------')
            sDateinameUndPfad = os.path.join(root, name)
            sDateiname = (os.path.join(name))
            sPruefsumme = scan(sDateinameUndPfad)
            #sTest = DatenzurueckGeben('c:\\temp\\ziel\\1.jpg')
            sDatenUndGroessen = DatenzurueckGeben(sDateinameUndPfad)
            print('funktion:    TempDBfuellen --> daten: sDatenUndGroessen',sDatenUndGroessen)

            print('sDateinameUndPfad  :' + sDateinameUndPfad + '      und sDateiname  :' + sDateiname + '      und sPrüfsumme: ' + sPruefsumme)

            if checkDateiInTempDBVorhanden(sPruefsumme) == None:
                sql = "INSERT INTO `Dateien` (`UNCPfad`, `Dateiname`, `Pruefsumme`, `DateinameNeu` ) VALUES (" \
                  "'" + sDateinameUndPfad + "', " \
                  "'" + sDateiname + "', " \
                  "'" + sPruefsumme + "', " \
                  "'" + sDatenUndGroessen + "')"
                
                print(sDatenUndGroessen)

                print('funktion:    TempDBfuellen --> daten: sql', sql)

                dbCursorTemp.execute(sql)
                conTemp.commit()
                print('wurde unter dieser ID ' + str(dbCursorTemp.lastrowid) + ' in die DB aufgenommen eingepflegt')                               # gibt die ID des letzten Eintrags zurück
            else:
                print('datei is scho da')
                #Baustelle - Logging:
                # hier wäre ein log nicht schlecht, nur dass man weiß, wieviele dateien im quellordner dubletten sind.

    print('-------- ende TempDBfuellen --------------------------------------------------------------')
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   TempDBfuellen Ende
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
#   hier gehts los ...
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

sDateinameUndPFad = sDateiname = sPruefsumme = "."
sDateinameUndPFad = sDateiname = sPruefsumme = sDatensatz = "."

walkVerzeichnis = "c:\\temp\\quelle\\"
#walkVerzeichnis = "C:\\01CM\\400 CM\\003_HandyBilder\\"
#walkVerzeichnis = "C:\\Temp\\quelle\\fehler1\\"
#walkVerzeichnis = "c:\\temp\\testumgebung\\"

sZielpfad = "c:\\temp\\Ziel\\"
usPadZielDB = "datenbanken/dbZiel.db"
usPadTempDB = "datenbanken/dbTemp.db"

#walkVerzeichnis = "I:\\000.Bilder.Sortiert"
#walkVerzeichnis = "C:\\01CM\\204_ProgrammiertesPython\\Testumgebung\\DateienNeu\\erledigt"

#Datenbanken verbinden:
conTemp = sqlite3.connect(usPadTempDB)
dbCursorTemp = conTemp.cursor()

conZiel = sqlite3.connect(usPadZielDB)
dbCursorZiel = conZiel.cursor()

## teil zum einlesen der tempdatenbank:
TempDBfuellen(walkVerzeichnis)

## teil zum kopieren der Bilder
BilderBearbeiten()

##print('------------- modul_ZielDBinit.auslesenOrdnerRekursiv --------------------------------------------------------------')
ZielDBfuellen(sZielpfad)
##print('-------- ende modul_ZielDBinit.auslesenOrdnerRekursiv --------------------------------------------------------------')
##
##conTemp.close()
##conZiel.close()
##
##datenbankZuruecksetzen(usPadTempDB)




























