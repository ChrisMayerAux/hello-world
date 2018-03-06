#!/usr/bin/python
# -*- coding: utf-8 -*-


from md5hash import scan
import os
import sqlite3
import shutil

import Class_lese_Config
import mod_check_Datei_In_TempDB_Vorhanden
import mod_check_Datei_In_ZielDB_Vorhanden


def BilderBearbeiten():
    """
    die Funktion BilderBearbeiten
        - arbeitet alle datensätze der temp datei ab,
        - je datensatz schaut es in die zieldb und sieht nach, ob der datensatz schon vorhanden ist
        - wenn nein wird die datei nach folgenden maßgaben
            - ordner mit bilddatumjahr.bilddatummonat wird erstellt
            - bild wird als '2012.07.04.10.34.09.jpg' dort abgespeichert
        - nocht nicht implementiert: bild wird in ordner: aufsHaendy\bilddatumjahr.bilddatummonat kopiert
    Übergabe: usTempDB
    Rückgabe: --
    """
    print('------------- BilderBearbeiten --------------------------------------------------------------')
    
    MeinePfade = Class_lese_Config.Pfade()
    conTemp = sqlite3.connect(MeinePfade.tempdb)
    dbCursorTemp = conTemp.cursor()
    dbCursorTemp.execute("SELECT * FROM `Dateien`")                 #Findet nimmt alle daten aus der datenbank Temp
    
    for datensatz in dbCursorTemp:                                   #und arbeitet sie ab
        #print(datensatz[4])                                         #gibt die Prüfsumme aus
        print('funktion:    BilderBearbeiten --> daten: datensatz[3](Prüfsumme): ',datensatz[3])

        #Übergibt die prüfsumme an PruefsummeInZielVorhanden bekommt ID zurück
        sPruefsumme = datensatz[3]
        sID = mod_check_Datei_In_ZielDB_Vorhanden.checkDateiInZielDBVorhanden(sPruefsumme)             


        if mod_check_Datei_In_ZielDB_Vorhanden.checkDateiInZielDBVorhanden(sPruefsumme) != None:

            #Datei bereits vorhanden.
            print("Datei vorhanden")#    + str(sID))
            print('funktion:    BilderBearbeiten --> daten: datensatz: ', datensatz)
       
        else:
            
##          hier müssen die entspechenden daten kopiert werden
            print("Datei nicht vorhanden")           
            print('funktion:    BilderBearbeiten --> daten: datensatz: ', datensatz)

##              prüfen ob ordner in zielstruktur vorhanden?                       - läuft
            sPfad = MeinePfade.zielpfad + (datensatz[4][:7])

            if os.path.exists(sPfad) == True:
                print(sPfad, "existiert.")
            else:
                print(sPfad, "existiert nicht.")
                os.mkdir(sPfad)

##            datei umbenennen und kopieren
            sQuellPfadUndDatei = datensatz[1]

##          hier die letzten 4 ziffern der prüfsumme in variable schreiben:
            #print(a[-5:])
            sPruefziffenteil = sPruefsumme[-2:]
            
            sZielPfadUndDatei = sPfad + '\\' + datensatz[4] + sPruefziffenteil + ("." + datensatz[2] [len(datensatz[2])-4:]).replace("..",".")

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

##            datei schrumpfen
            
    print('-------- ende BilderBearbeiten --------------------------------------------------------------')
            
