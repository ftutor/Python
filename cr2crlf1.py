#!/usr/bin/python
from __future__ import with_statement
import os
dir='/home/yingming.fang/project/assetcommander_git_repo/product/schema/'
#dir ='C:\\Yingming Fang\\project\\Python\\gitPython\\'
files = os.listdir(dir)


for file in files:
	if file.startswith('.')==False and file.endswith('Ui')==True:
		filename = dir+file
		output = dir+file
		print filename
		with open(filename, "rb") as f:
			s = f.read().replace('\r\n', '\n').replace('\r', '\n')

		with open(output,"wb") as out:
			out.write(s)
#    lines = s.split('\n')
