# coding: utf-8
#!/usr/bin/env python

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This script is a part of TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import mechanize
from re import search, sub
import cookielib
import requests
import time
import urllib2
import re
import os
import sys
from re import *
from urllib import *
from colors import *
from time import sleep

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

params = []

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

class UserAgent(FancyURLopener):
	version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'

useragent = UserAgent()
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

ctr=0
path_list = []
payloads = []

def sqlisearch0x00(web):

	os.system('clear')
	print R+'\n    ======================================'
	print R+'     S Q L i   H U N T E R (Auto Awesome)'
	print R+'    ======================================'
	print R+'  [It is recommended to run ScanEnum/Crawlers  '
	print R+'          before using this module] \n'
	
	with open('files/sql_payloads.lst','r') as pay:
	    for payload in pay:
		rem = payload
		rem = rem.replace('\n','')
		payloads.append(rem)
	
	br.open(web)
	web0 = web.strip('https://')
	web0 = web.strip('http://')
	try:
	        with open('tmp/'+web0+'-links.lst','r') as ro:
		    for r in ro:
			r = r.strip('\n')
			path_list.append(r)
	except IOError:
		print R+' [-] Path file not found!'
	
	def sqli_func(bugs):
	
	    global ctr
	    ctr = 0
	    if '?' in str(bugs) and '=' in str(bugs):
		for p in payloads:
		    bugs = bugs + str(p)
	    	    print B+" [*] Trying : "+C+ bugs
		    time.sleep(0.7)
	    	    response = requests.get(bugs).text
	    	    if (('error' in response) and ('syntax' in response) and ('SQL' in response)):
			print '\n'+G+' [+] Vulnerable link detected : ' + web
			print ''+R+' [*] Injecting payloads...'
			print ''+B+' [!] PoC : ' + str(bugs)
	    	        print ''+R+" [!] Payload : " + O + p + '\033[0m'
	    	        print "\033[1m [!] Code Snippet : \n\033[0m" + response + '\n'
			ctr = ctr + 1
	    else:
		print ''+GR+' [-] Link without parameter : '+B+'' + str(bugs)
	    if ctr > 0:
	        print '\n'+G+' [!] Congratulations! You have successfully found %s SQL bugs \033[0m\n' % ctr
	    else:
		print '\n'+R+' [-] No SQLi vulnerability found'

	for urli in path_list:
	    sqli_func(urli)

