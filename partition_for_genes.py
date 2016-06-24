
## this script devide the mtDNA into desired pieces 
## it uses fasta format file from multiple alignment


import re
import sys
import os


FASTA = open("FASTA.txt", "r+")
CR = open("CR.fasta", "w")
s12RNA = open("12sRNA.fasta", "w")
s16RNA = open("16sRNA.fasta", "w")
tRNA = open("tRNAs.fasta", "w")
ND1 = open("ND1.fasta", "w")
ND2 = open ("ND2.fasta", "w")
COX1 = open("COX1.fasta", "w")
COX2 = open("COX2.fasta", "w")
ATP8 = open("ATP8.fasta", "w")
ATP6 = open("ATP6.fasta", "w")
COX3 = open("COX3.fasta", "w")
ND3 = open("ND3.fasta", "w")
ND4L = open("ND4L.fasta", "w")
ND4 = open("ND4.fasta", "w")
ND5 = open("ND5.fasta", "w")
ND6revcomp = open("ND6revcomp.fasta", "w")
CYTB = open("CYTB.fasta", "w")



for seq in FASTA.readlines():
    if re.search(r">",seq):
        name = seq.strip()
##        dloop.write("%s\n"%(name))
        CR.write("%s\n"%(name))
        s12RNA.write("%s\n"%(name))
        s16RNA.write("%s\n"%(name))
        tRNA.write("%s\n"%(name))
        ND1.write("%s\n"%(name))
        ND2.write("%s\n"%(name))
        COX1.write("%s\n"%(name))
        COX2.write("%s\n"%(name))
        ATP8.write("%s\n"%(name))
        ATP6.write("%s\n"%(name))
        COX3.write("%s\n"%(name))
        ND3.write("%s\n"%(name))
        ND4L.write("%s\n"%(name))
        ND4.write("%s\n"%(name))
        ND5.write("%s\n"%(name))
        ND6revcomp.write("%s\n"%(name))
        CYTB.write("%s\n"%(name))

    else:
        seq = seq.strip()
        Dloop1 = seq[0:576]
        tRNA1Phe = seq[576:647]
        sRNA12 = seq[647:1601]
        tRNA2Val = seq[1601:1670]
        sRNA16 = seq[1670:3229]
        tRNA3Leu = seq[3229:3304]
        intergenic1 = seq[3304:3306]
        NDone = seq[3306:4260] #Taken from Hoviks file
        intergenic2 = seq[4260:4262]
        tRNA4Ile = seq[4262:4331]
        tRNA5Glu = seq[4328:4400]
        intergenic3 = seq[4400:4401]
        tRNA6Meth = seq[4401:4469]
        NDtwo = seq[4469:5510] #Taken from Hoviks file
        intergenic4 = seq[5510:5511] 
        tRNA7Try = seq[5511:5579]
        intergenic5 = seq[5579:5586]
        tRNA8Ala = seq[5586:5655]
        intergenic6 = seq[5655:5656]
        tRNA9Asp = seq[5656:5729]
        intergenic7 = seq[5729:5760]
        tRNA10Cys = seq[5760:5826]
        tRNA11Tyr = seq[5825:5891]
        intergenic8 = seq[5891:5903]
        COXone = seq[5903:7442] #Taken from Hoviks file
        intergenic9 = seq[7442:7445]
        tRNA12Ser = seq[7445:7514]
        intergenic10 = seq[7514:7517]
        tRNA13Asp = seq[7517:7585]
        COXtwo = seq[7585:8266] #Taken from Hoviks file
        intergenic11 = seq[8266:8294]
        tRNA14Lys = seq[8294:8364]
        intergenic12 = seq[8364:8365]
        ATPeigth = seq[8365:8569]#Taken from Hoviks file
        ATPsix = seq[8526:9204]#Taken from Hoviks file
        intergenic13 = seq[9204:9206]
        COXthree = seq[9206:9989]
        intergenic14 = seq[9989:9990]
        tRNA15Gly = seq[9990:10058]
        NDthree = seq[10058:10403]#Taken from Hoviks file
        intergenic15 =seq[10403:10404]
        tRNA16Arg = seq[10404:10469]
        NDfourL = seq[10469:10763]#Taken from Hoviks file
        NDfour = seq[10759:12136]#Taken from Hoviks file
        intergenic16 = seq[12136:12137]
        tRNA17His = seq[12137:12206]
        tRNA18Ser = seq[12206:12265]
        tRNA19Leu = seq[12265:12336]
        NDfive = seq[12336:14145]#Taken from Hoviks file
        intergenic17 = seq[14145:14150]
        NDsixrevcomp = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[14672:14150:-1] #Taken from Hoviks file
        intergenic18 = seq[14672:14673]
        tRNA20Gln = seq[14673:14742]
        intergenic19 = seq[14742:14746]
        CYTb = seq[14746:15886]#Taken from Hoviks file
        intergenic20 = seq[15886:15887]
        tRNA21Thre = seq[15887:15953]
        intergenic21 = seq[15953:15955]
        tRNA22Pro = seq[15955:16023]
        Dloop2 = seq[16023:16400]
        CR.write("%s%s\n"%(Dloop2,Dloop1))
        s12RNA.write("%s\n"%(sRNA12))
        s16RNA.write("%s\n"%(sRNA16))
        tRNA.write("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n"%(tRNA1Phe,tRNA2Val,tRNA3Leu,tRNA4Ile,tRNA5Glu,tRNA6Meth,tRNA7Try,tRNA8Ala,tRNA9Asp,tRNA10Cys,tRNA11Tyr,tRNA12Ser,tRNA13Asp,tRNA14Lys,tRNA15Gly,tRNA16Arg,tRNA17His,tRNA18Ser,tRNA19Leu,tRNA20Gln,tRNA21Thre,tRNA22Pro))
        ND1.write("%s\n"%(NDone))
        ND2.write("%s\n"%(NDtwo))
        COX1.write("%s\n"%(COXone))
        COX2.write("%s\n"%(COXtwo))
        ATP8.write("%s\n"%(ATPeigth))
        ATP6.write("%s\n"%(ATPsix))
        COX3.write("%s\n"%(COXthree))
        ND3.write("%s\n"%(NDthree))
        ND4L.write("%s\n"%(NDfourL))
        ND4.write("%s\n"%(NDfour))
        ND5.write("%s\n"%(NDfive))
        ND6revcomp.write("%s\n"%(NDsixrevcomp))
        CYTB.write("%s\n"%(CYTb))

CR.close()
s12RNA.close()
s16RNA.close()
tRNA.close()
ATP6.close()
ATP8.close()
COX1.close()
COX2.close()
COX3.close()
CYTB.close()
ND1.close()
ND2.close()
ND3.close()
ND4L.close()
ND4.close()
ND5.close()
ND6revcomp.close()
        

