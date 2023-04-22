#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
os.path.abspath(__file__)
import credit
import colorama
from colorama import Fore, Back, Style, init
init()
import sys
from tqdm import tqdm
if sys.version_info[0] < 3:
    print (Fore.RED+'''\n [!] You have to install python 3.X to use this script.\n\n'''
    	+Fore.GREEN+'''instructions:\n\n''' 
    	+Fore.YELLOW+'''	Linux: apt install python3
    	Windows: https://www.python.org/downloads/\n\n'''
		+Fore.GREEN+'''Usage:'''
    	+Fore.YELLOW+'''
    	python3 pupi.py
    	py -3 pupi.py''')
    sys.exit()


print(Fore.GREEN+credit.getCredits()[0])
print (Fore.BLUE+'Forked from Pupi.py')
print()

FN=input(Fore.YELLOW+'Enter your first name: ' +Fore.WHITE)
FN=FN.lower()
LN=input(Fore.YELLOW +'Enter your last name: '+Fore.WHITE)
LN=LN.lower()
SN=input(Fore.YELLOW +'Enter your surname: '+Fore.WHITE)
SN=SN.lower()
KN = input(Fore.YELLOW +'Enter  other name: '+Fore.WHITE)
KN=KN.lower()
PN = input(Fore.YELLOW +'Enter nickname: '+Fore.WHITE)
PN = PN.lower()
while True:
		try:
			AG=input(Fore.YELLOW +'Enter your age: '+Fore.WHITE)
			if not int(AG) or len(AG)>3:
				raise ValueError()
		except ValueError:
		    print (Fore.RED +'invalid age. Please try again!'+Fore.WHITE)
		else:
			break
while True:
		try:
			PG=input(Fore.YELLOW +'Enter phone number: '+Fore.WHITE)
			PR=input(Fore.YELLOW +'Enter another phone number: '+Fore.WHITE)
			PU=input(Fore.YELLOW +'Enter maiden phone number: '+Fore.WHITE)
			if not int(PG) or len(PG)<3:
				raise ValueError()
		except ValueError:
		    print (Fore.RED +'invalid phone number. Please try again!'+Fore.WHITE)
		else:
			break
while True:
		try:
			BI=input(Fore.YELLOW +'Enter your birthyear: '+Fore.WHITE)
			if not int(BI) or len(BI)!=4:
				raise ValueError()
		except ValueError:
			print (Fore.RED +'please, enter a valid birthyear.example is 1974'+Fore.WHITE)
		else:
			break
BI = str(BI)
print (Fore.GREEN+'''\n [##]This script will generate an awesome password list for you\n\n'''
    	+Fore.GREEN+'''i:\n\n''' )
print()

Result1= str(FN+LN+SN+AG)

def progress():
    for i in tqdm(range(10000)):
         pass
     
pass1=FN
pass2=LN
pass3=SN
pass4=KN
pass5=PN
	# real batch
pass6=FN[0].capitalize() + FN[1:]
pass7=LN[0].capitalize() + LN[1:]
pass8=SN[0].capitalize() + SN[1:]
pass9=KN[0].capitalize() + KN[1:]
pass10=PN[0].capitalize() + PN[1:]
	# second batch
pass101=FN + BI
pass102=LN + BI
pass103=SN + BI
pass104=KN + BI
pass105=PN + BI
	# again batch
	# real batch
pass110= KN + FN
pass111 = KN + PN
pass112 = FN + LN
pass113= KN + FN
pass114= SN + KN
pass106= pass6+BI
pass107= pass7+ BI
pass108= pass8 + BI
pass109=KN[0].capitalize() + KN[1:] + BI
pass100=PN[0].capitalize() + PN[1:] + BI
	# second batch
park = PG
park2 = PR
park3 = PU


print ()
# Simple & .upper(), & .capitalize(),
list=[ park,park2,park3,pass110,pass114,pass1,pass2,pass3,pass4,pass5,pass6,pass7,pass8,pass9,pass10,pass100,pass101,pass102,pass103,pass104,pass105,pass106,pass107,pass108,pass109,pass111,pass112,pass113]








#print (Fore.BLUE+'\n'.join(liste))
password_file =input("Name of wordlist file e.g pass.txt :  ")
my_file = open(password_file, 'w')
my_file.write(str('\n'.join(list)))
progress()
my_file.close()

print (Fore.RED+''' 
	####################################################
	#                                                  #
	#  '''+Fore.GREEN+'''All passwords are saved in ''' +  password_file+  ''' file!'''.center(4,'#')+Fore.RED+'''  #
	#                                                  #
	####################################################'''+Fore.WHITE)
print (Fore.MAGENTA +'Thanks for using Wordbeast')


