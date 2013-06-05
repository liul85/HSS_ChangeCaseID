#!/usr/bin/python

import re, sys, os, string

def ReplaceCaseID(filefullpath,filename):
	filetruename = filename[:len(filename)-4]
	ModificationCaseID = '        CaseID "' + filetruename + '"\n'
	oldcaseId = ''
	f = open(filefullpath)
	for line in f.readline():
		if line.find("CaseID") != -1:
			oldcaseId = line
			break
	Data = f.read()
	Data = re.sub(oldcaseId, ModificationCaseID, Data)
	f.close()
	open(filefullpath,'w+b').write(Data)


def main():
	if len(sys.argv) != 2:
		print 'Usage: HSS_ChangeCaseiD.py folder'
		sys.exit(100)

	files = os.walk(sys.argv[1])
	a = 0
	for path, subdirs, f in files:
		for file in f:
			print "Now processing ", file , "...."
			filefullname = os.path.join(path,file)
			ReplaceCaseID(filefullname,file)
			a += 1
	print "Totally process ", a, "files"


if __name__ == '__main__':
	main()
