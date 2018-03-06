#!/usr/bin/python
# -*- coding: utf-8 -*-


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   DateiZeitUmwandeln
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def DateiZeitUmwandeln(UeberGabeString):
    """
    die Funktion DateiZeitUmwandeln wandelt den übergabestring in ein datum/zeitstring um
    Übergabe: Baustelle: pattern des übergabesting eintragen
    Rückgabe: datum als string
    """
    return  strftime("%Y.%m.%d.%H.%M.%S" ,time.localtime(UeberGabeString))
