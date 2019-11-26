#!/usr/bin/python
#This script will compile the qstat data and is expected to be run every 15-20 minutes everyday
import os
import os.path
import time
import csv
import sys
import datetime

#file named according to current time - year/month/day - hour/minute
timeOUT = time.strftime("%Y%m%d-%H%M")
timeLine = time.strftime("%Y-%m-%d-%H:%M")

#Save Location
outDIR = "/root/metrics/OUT/"
filename = outDIR+timeOUT+".csv" #saved as csv (comma separated value)

#uses command qstat-f
p = os.popen('qstat -f',"r")

#Checks if file exists, if not, it writes 
if not os.path.exists(filename):

	# Check for 'queuename' in the first line of the input from qstat. If it's there skip that line. 
	# If it's not there exit the program and write nothing.
	if "queuename" in p.readline(): p.readline(+1)
	else: sys.exit()

	#saves file
	filemain = open(filename,"w") 
	print (filemain)

	while 1:

		#read line-by-line
		line = p.readline()
		if not line: break

		#eliminates spaces, dashes, etc to make file readible for csv
		line =(line.replace('                      ',',').replace('/',',').replace('                  ',',').replace('          ',',').replace('     ',',').replace('    ',',').replace(' ',',').replace('-','').replace(' ',''))
		cleanedLine = line.strip()#removes whitespaces
		if cleanedLine:
			
			#writes file
			filemain.write(timeLine+","+line)
	filemain.close()

elif os.path.exists(filename):	
	
	#If script is run twice in one minute, names conflict
	redo = timeOUT+"*Error.txt"
	
	#Save Location
	create = open(outDIR+redo, 'w')
	create.write('Error- The script was run irregularily please wait a minute to try again. This error occurred at:'+timeLine)


