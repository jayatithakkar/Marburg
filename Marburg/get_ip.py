#!/usr/bin/env python3

import threading
import subprocess
import re

flag = False

def getIP():
    global ip, flag
    while True:
        if flag:
            return ip
        else:
            pass

def task(n, cmd):
    global ip, flag
    temp = cmd + str(n)
    res = subprocess.Popen(("ping -c 1 " + temp), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    res = res.stdout.read().decode()
    if 'Destination Host Unreachable' in res or 'Request Timed Out' in res:
        pass
    else:
        ip.append(temp)
    if n == 254:
        flag = True
cmd = 'sudo ifconfig'
cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.read()
temp = re.findall('inet (.+)  netmask', str(cmd))
temp = temp[0].split('.')
network = temp[0] + "."+ temp[1] + "." + temp[2] + "."
ip = []
for i in range(1,255):
    t = threading.Thread(name = i, target = task, args = (i, network))
    t.daemon = False
    t.start()



