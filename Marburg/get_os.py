#!/usr/bin/env python3

import nmap3

def getos(host):
    nm = nmap3.Nmap()
    res = nm.nmap_os_detection(host)
    return res[0]['osclass']['vendor']
