#!/usr/bin/python
# -*- coding: utf-8 -*-


from md5hash import scan

def machHash(usDateiMitPfad):
    return(scan(usDateiMitPfad))


print(machHash('c:\\temp\\quelle\\quelle.avi'))
print(machHash('c:\\temp\\quelle\\quelle.jpg'))
print(machHash('c:\\temp\\quelle\\quelle2.jpg'))
print(machHash('c:\\temp\\quelle\\quelle3.jpg'))
