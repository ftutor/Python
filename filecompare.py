import os
import sys
import subprocess
#dir = 'C:/Yingming Fang/verify'
#fi = open(dir+os.sep+'adminB.txt','Ur+')
#fo = open(dir+os.sep+'adminTest.txt','Ur+')
def fileComp(input, output,log):
	start = input.rfind('/')
	filename = input[start+1:len(input)]
	log.write('benchmark file is :'+input+'\n')
	log.write('cmp file is '+output+'\n')
	fi = open(input,'Ur+')
	fo = open(output,'Ur+')
	benchmark = fi.readlines()
	out = fo.readlines()
	print "items in bechmark: %s are %s" % (input,str(len(benchmark)))
	log.write('items in bechmark:'+str(input)+' is :'+str(len(benchmark))
	print "item in outfile: %s are %s ",(output,str(len(out)))
	
	log.write('items in outfile:'+str(output)+' is :'+str(len(out))
	count =0
	for each in benchmark:
		for single in out:
			if each.strip()==single.strip():
				count=count+1
	print 'there are %d items contained in output file ' %count
	log.write('there are:'+str(count)+' items contained in output file')
	fi.close()
	fo.close()

par1 = sys.argv[1]
par2 = sys.argv[2]
filelist = os.listdir(par1)
logfile ='log.txt'
log =open(logfile,'w+')
for file in filelist:
	start = file.rfind('/');
	filename = file[start+1:len(file)]
	print filename
	inputfile=filename+'B.txt'
	cmpfile=filename+'Test.txt'
	input = open(inputfile,'w+')
	output = open(cmpfile,'w+')
	subprocess.call(['ls','-tral'],stdout=input)
	subprocess.call(['ls','-tral'],stdout=output)
	fileComp(input+os.sep+filename,output+os.sep+filename,log)
	input.close()
	output.close()
log.close()
#	fileComp(input+os.sep+filename,output+os.sep+filename,log)

