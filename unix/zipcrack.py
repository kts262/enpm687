#!/usr/bin/python

import zipfile, sys

zipfile = zipfile.ZipFile(sys.argv[1])
wordlist = open('wordlist.txt')
for word in wordlist:
	password = word.strip('\n')
	print "Trying: " + password 
	try:
		zipfile.extractall(pwd=password)
		print "[!] The password is: " + password + "\n"
		exit(0)
	except Exception, e:
		pass
