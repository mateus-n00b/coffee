'''
Programa para decifrar os arquivos encriptados pelo programa coffee.py.
Forma de uso vide README.md. 

Mateus-n00b, Agosto 2016

Versao 1.0

Licenca GPL

Execute:os.system('for x in *; do if grep h4ck3d <<< $x &> /dev/null; then echo $x >> /tmp/aux; fi ;done')

'''

import os,sys,time

try:
	from Crypto.Cipher import AES
except:
	  os.system('pip install pycrypto')
	  time.sleep(1)
	  from Crypto.Cipher import AES
	  
from Crypto.Random import random

PASSWORD = raw_input("pass> ")
IV = raw_input("iv> ")

bar = AES.new(PASSWORD, AES.MODE_CBC,str(IV))		

aux = open("/tmp/aux",'r')
cont = 0
foo = ""

for x in aux.readlines():
	try:
		x = x.rstrip()
		ini = 1
		fin = 16
		decr = open(x, 'r')
		new_file = open("%s_decrypted" % x, 'w')	
		new_file.write(bar.decrypt(decr.read()))	
		new_file.close()
		decr.close()	
	except:
		print "Error to decrypt %s" % x
	
