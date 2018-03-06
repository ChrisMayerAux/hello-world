#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import exifread
from contextlib import suppress
import mod_ExifZeit_Umwandeln
import time, locale
from time import gmtime, strftime



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   DatenzurueckGeben
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def DatenzurueckGeben(usDateinameUndPfad):
    """
    die Funktion DatenzurueckGeben
        - liest die exif-daten, zieht die daten: sDatumZeitOrginal, sDatumZeitDigitalisiert, sDatumZeitBild 
        - liest die datei daten, zieht die daten: sDatumZeitDateiatime, sDatumZeitDateimtime, sDatumZeitDateictime
        - nimmt das älteste datum und gibt es als datum formatiert zurück
    Übergabe: usDateinameUndPfad
    Rückgabe: datum als Baustelle: typ eintragen  format %Y.%m.%d.%H.%M.%S"
    """

    sDateinameUndPfad = usDateinameUndPfad
    ##print('1 funktion:    DatenzurueckGeben --> daten: sDateinameUndPfad',sDateinameUndPfad)    
    # datei öffnen für exif read
    f = open(sDateinameUndPfad, 'rb')
    #und lesen
    tags = exifread.process_file(f)

    # und wenn es keinen tag gibt
    sDatumZeitOrginalEpoch= sDatumZeitDigitalisiertEpoch = sDatumZeitBildEpoch = sDatumZeitDateiatime = sDatumZeitDateimtime = sDatumZeitDateictime =  2082708673                     #datum auf 2038 gestellt ...
    sBildbreite = sBildhoehe = 0
    ##print('2 funktion:    DatenzurueckGeben --> daten: sDateinameUndPfad',sDateinameUndPfad)
    
    with suppress(KeyError):

        #exif zeug lesen und zeiten umwandeln
        pattern = '%Y.%m.%d.%H.%M.%S'

        sDatumZeitOrginal = mod_ExifZeit_Umwandeln.ExifZeitUmwandeln((tags["EXIF DateTimeOriginal"]))
        sDatumZeitOrginal = sDatumZeitOrginal.replace("2000.00.00.00.00.00", "2038.01.01.01.01.01")
        sDatumZeitOrginal = sDatumZeitOrginal.replace("0000.00.00.00.00.00", "2038.01.01.01.01.01")
        #print('sDatumZeitOrginal',sDatumZeitOrginal)
        sDatumZeitOrginalEpoch = int(time.mktime(time.strptime(sDatumZeitOrginal, pattern)))
        
        sDatumZeitDigitalisiert = mod_ExifZeit_Umwandeln.ExifZeitUmwandeln((tags["EXIF DateTimeDigitized"]))
        sDatumZeitDigitalisiert = sDatumZeitDigitalisiert.replace("2000.00.00.00.00.00", "2038.01.01.01.01.01")
        sDatumZeitDigitalisiert = sDatumZeitDigitalisiert.replace("0000.00.00.00.00.00", "2038.01.01.01.01.01")
        #print('sDatumZeitOrginal',sDatumZeitOrginal)
        sDatumZeitDigitalisiertEpoch = int(time.mktime(time.strptime(sDatumZeitDigitalisiert, pattern)))
        
        sDatumZeitBild = mod_ExifZeit_Umwandeln.ExifZeitUmwandeln((tags["Image DateTime"]))
        sDatumZeitBild = sDatumZeitBild.replace("2000.00.00.00.00.00", "2038.01.01.01.01.01")
        sDatumZeitBild = sDatumZeitBild.replace("0000.00.00.00.00.00", "2038.01.01.01.01.01")
        #print('sDatumZeitOrginal',sDatumZeitOrginal)
        sDatumZeitBildEpoch = int(time.mktime(time.strptime(sDatumZeitBild, pattern)))
        
        #sBildbreite = (tags["EXIF ExifImageWidth"])
        #sBildhoehe = (tags["EXIF ExifImageLength"])

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
    ##print('funktion:    DatenzurueckGeben --> daten: rückgabe: ',a)
    return a
