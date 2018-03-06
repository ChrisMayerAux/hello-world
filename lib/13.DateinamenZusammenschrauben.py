#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time, locale

sQuellPfad = "c:\\temp\\Quelle\\"
sZielPfad = "c:\\temp\\Ziel\\"

sDateiname = "."

def ErstelleZeitstempel(usDateiMitPFad): 
    # -> hol den zeitstempel der datei -> creation
    timestamp = (os.path.getmtime(usDateiMitPFad))
    datetime = time.localtime(timestamp)

    # --> hier die 
    sTag = (time.strftime("%d", datetime))
    sMonat = (time.strftime("%m", datetime))
    sJahr = (time.strftime("%Y", datetime))
    sStunde = (time.strftime("%H", datetime))
    sMinute = (time.strftime("%M", datetime))
    sSekunde = (time.strftime("%S", datetime))

    return  sJahr + "_" + sMonat + "_" + sTag + "_" + sStunde + "_" + sMinute + "_" + sSekunde  


file = ('c:\\temp\\quelle\\quelle.jpg')
sDateiname = (ErstelleZeitstempel(file)+ '.jpg')

print(sDateiname)



