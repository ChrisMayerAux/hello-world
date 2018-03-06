#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

def auslesenOrdnerRekursiv(walk_dir):
    for root, dirs, files in os.walk(walk_dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        #for name in dirs:
            #print(os.path.join(root, name))


walkVerzeichnis = "c:\\temp\\quelle\\"
auslesenOrdnerRekursiv(walkVerzeichnis)


