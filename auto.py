# this script make the frequency Arlequin unpit file
import sys
import os

#file = sys.argv[1] 
#out = sys.argv[2]

file = open("all_pops.txt", "r+")
output = open("1.arp", "w")



counter = 0
for eachline in  file.readlines():
	counter += 1
file.seek(0,0)  # reset the file


output.write("%s\n\tTitle = %s"%("[Profile]",'"New_project"'))
output.write("\n\tNbSamples = %s"%(counter))
output.write("\n\tDataType = %s"%("FREQUENCY"))
output.write("\n\tGenotypicData = %s"%("0"))
output.write("\n\tLocusSeparator = %s"%("Tab"))
output.write("\n\tGameticPhase = %s"%("1"))
output.write("\n\tFrequency = %s"%("REL"))
output.write("\n%s"%("[Data]"))
output.write("\n%s"%("[[Samples]]"))

for eachline in file.readlines():
	eachline=eachline.rstrip().split("\t")
	i=1
	j=1
	#print '\tSampleName = "%s"\n\tSampleSize = %s\n\tSampleData = {' % #(eachline[0],eachline[-1])
	output.write('\n\tSampleName = "%s"\n\tSampleSize = %s\n\tSampleData = {'%(eachline[0],eachline[-1]))
	for eachel in eachline:	
		#print j,"\t",eachline[i]
		output.write("\n%s\t%s"%(j,eachline[i]))
		#print len(eachline)
		if i < int(len(eachline) - 2):
			i=i+1
			#print i
			j=j+1
			#print j
		else:
			#print "}"
			output.write("\n%s"%("}"))
			break
