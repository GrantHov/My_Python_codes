
## this script devide the mtDNA into desired pieces 
## it uses fasta format file from multiple alignment


import re
import sys
import os

##inputfile = sys.argv[1]
#FASTA = sys.argv[2]
#Partitioned_file = sys.argv[3]

fastafile = open("test.txt", "r+")
outfile = open("FASTA.txt", "w")
for eachline in fastafile.readlines():
        if re.search(r">",eachline):
                outfile.write("\n%s"% (eachline))
        else:
                eachline = eachline.strip()
                outfile.write(eachline)
                
fastafile.close()
outfile.close()
file2 = open("FASTA.txt", "r+")
Control_region = open("Control_region.fasta", "w")
RNA_file = open("RNA_file.fasta", "w")
First_nucleotide = open("First_nucleotide.fasta", "w")
Second_nucleotide = open("Second_nucleotide.fasta", "w")
Third_nucleotide = open("Third_nucleotide.fasta", "w")




for seq in file2.readlines()[1:]:
    if re.search(r">",seq):
            
                name = seq.strip()
                Control_region.write("%s\n"%(name))
                RNA_file.write("%s\n"%(name))
                First_nucleotide.write("%s\n"%(name))
                Second_nucleotide.write("%s\n"%(name))
                Third_nucleotide.write("%s\n"%(name))
    else:
                seq = seq.strip()
                Dloop1 = seq[0:576]
                tRNA1Phe = seq[576:647]
                sRNA12 = seq[647:1601]
                tRNA2Val = seq[1601:1670]
                sRNA16 = seq[1670:3229]
                tRNA3Leu = seq[3229:3304]
                intergenic1 = seq[3304:3306]
                ND1 = seq[3306:4260] #Taken from Hoviks file
                intergenic2 = seq[4260:4262]
                tRNA4Ile = seq[4262:4331]
                tRNA5Gln = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[4399:4330:-1] # NO OVERLAP
                intergenic3 = seq[4400:4401]
                tRNA6Meth = seq[4401:4469]
                ND2 = seq[4469:5510] #Taken from Hoviks file
                intergenic4 = seq[5510:5511] 
                tRNA7Try = seq[5511:5579]
                intergenic5 = seq[5579:5586]
                tRNA8Ala = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[5654:5585:-1]
                intergenic6 = seq[5655:5656]
                tRNA9Asp = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[5728:5655:-1]
                intergenic7 = seq[5729:5760]
                tRNA10Cys = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[5825:5759:-1]
                tRNA11Tyr = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[5890:5825:-1] # NO OVERLAP
                intergenic8 = seq[5891:5903]
                COX1 = seq[5903:7442] #Taken from Hoviks file
                intergenic9 = seq[7442:7445]
                tRNA12Ser = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[7513:7444:-1]
                intergenic10 = seq[7514:7517]
                tRNA13Asp = seq[7517:7585]
                COX2 = seq[7585:8266] #Taken from Hoviks file
                intergenic11 = seq[8266:8294]
                tRNA14Lys = seq[8294:8364]
                intergenic12 = seq[8364:8365]
                ATP8 = seq[8365:8569]#Taken from Hoviks file
                ATP6 = seq[8526:9204]#Taken from Hoviks file
                intergenic13 = seq[9204:9206]
                COX3 = seq[9206:9989]
                intergenic14 = seq[9989:9990]
                tRNA15Gly = seq[9990:10058]
                ND3 = seq[10058:10403]#Taken from Hoviks file
                intergenic15 =seq[10403:10404]
                tRNA16Arg = seq[10404:10469]
                ND4L = seq[10469:10763]#Taken from Hoviks file
                ND4 = seq[10759:12136]#Taken from Hoviks file
                intergenic16 = seq[12136:12137]
                tRNA17His = seq[12137:12206]
                tRNA18Ser = seq[12206:12265]
                tRNA19Leu = seq[12265:12336]
                ND5 = seq[12336:14145]#Taken from Hoviks file
                intergenic17 = seq[14145:14150]
                ND6revcomp = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[14672:14150:-1] #Taken from Hoviks file
                intergenic18 = seq[14672:14673]
                tRNA20Glu = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[14741:14672:-1]
                intergenic19 = seq[14742:14746]
                CYTB = seq[14746:15886]#Taken from Hoviks file
                intergenic20 = seq[15886:15887]
                tRNA21Thre = seq[15887:15953]
                intergenic21 = seq[15953:15955]
                tRNA22Pro = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[16022:15954:-1]
                Dloop2 = seq[16023:]

                All_genes = ND1 + ND2  + COX1 + COX2 + ATP8 + ATP6 + COX3 + ND3 + ND4L +ND4 + ND5+ CYTB + ND6revcomp
                splited_All_genes = re.findall('..?.?',All_genes)
##                print All_genes
                All_genes_1_nucl = list()
                All_genes_2_nucl = list()
                All_genes_3_nucl = list()
                
                for nucl in splited_All_genes:
                        All_genes_1_nucl.append(nucl[0])
                        All_genes_2_nucl.append(nucl[1])
                        All_genes_3_nucl.append(nucl[2])
                        
                All_genes_1_nucl = ''.join(All_genes_1_nucl)
                All_genes_2_nucl = ''.join(All_genes_2_nucl)
                All_genes_3_nucl = ''.join(All_genes_3_nucl)
##                print All_genes_third_nucl

                
                Third_nucleotide.write("%s\n"%(All_genes_3_nucl))
                Second_nucleotide.write("%s\n"%(All_genes_2_nucl))
                First_nucleotide.write("%s\n"%(All_genes_1_nucl))
                Control_region.write("%s%s\n"%(Dloop1,Dloop2))
                RNA_file.write("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n"%(sRNA12,sRNA16,tRNA1Phe,tRNA2Val,tRNA3Leu,tRNA4Ile,tRNA5Gln,tRNA6Meth,tRNA7Try,tRNA8Ala,tRNA9Asp,tRNA10Cys,tRNA11Tyr,tRNA12Ser,tRNA13Asp,tRNA14Lys,tRNA15Gly,tRNA16Arg,tRNA17His,tRNA18Ser,tRNA19Leu,tRNA20Glu,tRNA21Thre,tRNA22Pro,intergenic1,intergenic2,intergenic3,intergenic4,intergenic5,intergenic6,intergenic7,intergenic8,intergenic9,intergenic10,intergenic11,intergenic12,intergenic13,intergenic14,intergenic15,intergenic16,intergenic17,intergenic18,intergenic19,intergenic20,intergenic21))

Third_nucleotide.close()
Second_nucleotide.close()
First_nucleotide.close() 
Control_region.close()
RNA_file.close()
