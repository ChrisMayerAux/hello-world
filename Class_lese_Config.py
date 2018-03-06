class Pfade:
    quellpfad = ""
    zielpfad = ""
    tempdb = ""
    zieldb = ""

 
    def __init__(self):

        path="konfiguration.cfg"
        aArray={}

        #Datei öffnen
        d = open(path)

        #inhalt nach zeilen auslesen
        content = d.readlines()

        #durchwandern der zeilen
        for line in content:
            #leerzeichen entfernen:
            sOhneLeerzeichen = line.replace(" ", "")
            sOhneUmbrueche = sOhneLeerzeichen.replace('\r', '')
            sOhneUmbrueche = sOhneLeerzeichen.replace('\n', '')
            sOhneLeerzeichen = sOhneUmbrueche.replace(" ", "")           
            #zerlegen des strings nach '='
            a=sOhneLeerzeichen.split("=")
            #zuweisen von schlüssel und wert in das Dictionary
            aArray[a[0]] = a[1]

        #datei zumachen    
        d.close

        for Schluessel in aArray:
            #print("for Schluessel in aArray:",Schluessel)
            if Schluessel =="quellpfad":
                self.quellpfad = aArray[Schluessel]
            elif Schluessel =="zielpfad":
                self.zielpfad = aArray[Schluessel]    
            elif Schluessel =="tempdb":
                self.tempdb = aArray[Schluessel]  
            elif Schluessel =="zieldb":
                self.zieldb = aArray[Schluessel]  
 
    def printState(self):
        print("quellpfad  = " + self.quellpfad)
        print("zielpfad = " + str(self.zielpfad))
        print("tempdb = " + str(self.tempdb))
        print("zieldb = " + str(self.zieldb)) 


#MeinePfade = Pfade()
#MeinePfade.printState()
#print('MeinePfade.quellpfad',MeinePfade.quellpfad) 
