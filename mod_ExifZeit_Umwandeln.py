#!/usr/bin/python
# -*- coding: utf-8 -*-


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   ExifZeitUmwandeln
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ExifZeitUmwandeln(UeberGabeString):
    """
    die Funktion ExifZeitUmwandeln wandelt den übergabestring in ein datum/zeitstring um
    Übergabe: Baustelle: pattern des übergabesting eintragen
    Rückgabe: datum als string
    """
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
