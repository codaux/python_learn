import requests
import bs4
import re
import os
import random
import time
import re
from urllib import parse
from bs4 import BeautifulSoup as soup
import socket
import string
import threading
import pyhera
import subprocess
import base64


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#channels = [ 'v2rray' , 'freeland8' , 'payam_nsi'  ]
chann = [
'https://t.me/s/DarkTeam_VPN',
'https://t.me/s/IraneAzad_Net',
'https://t.me/s/v2rayng_org',
'https://t.me/s/v2rray',
'https://t.me/s/freeland',
'https://t.me/s/payam_nsi',
'https://t.me/s/AzadiVPNs',
'https://t.me/s/V2rayNG_Outline',
'https://t.me/s/Outline_Vpn',
'https://t.me/s/freeland8',
'https://t.me/s/beshkan',
'https://t.me/s/v2rayng_fa',
'https://t.me/s/FalconPolV2rayNG']
chann64 = [
'https://raw.githubusercontent.com/ssrsub/ssr/master/trojan',
'https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray',
'https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub',
'https://raw.githubusercontent.com/clashconfig/UFO/main/UFO_base.txt',
'https://raw.githubusercontent.com/rezasamaniiii/ss/main/ss.txt',
'https://git.io/darkb' ]

def ex(c):
    all = []
    vmess = re.findall('>(vmess:.+?)[<]' , c)
    vless = re.findall('>(vless:.+?)[<]' , c)
    ss = re.findall('>(ss:.+?)[<]' , c)
    trojan = re.findall('>(trojan:.+?)[<]' , c)
    sn = re.findall('>(sn:.+?)[<]' , c)
    xray =  re.findall('>(xray:.+?)[<]' , c)
    wireguard =  re.findall('>(wireguard:.+?)[<]' , c)
    all = vmess + vless + ss + trojan + sn + xray + wireguard 
    print(all)
    return all

alls = []
p = { 'socks5' : '127.0.0.1:10808' } 
for x in chann:
    #url = "https://t.me/s/" + x + '/'
    #print(url)
    c = requests.get (x , headers = headers).text
    d = ex(c)
    #print(d)
    alls = alls + d
#print(alls)
    
for x in chann64:    
    w = requests.get (x , headers = headers).text
    #print(w)
    w = base64.b64decode(w)
    #wx = w.split('\r\n')
    print(w)
    #zz = ex(w)
    #alls = alls + ex(w);

#print(txt)
#print('xxxxxxxxxxxxxxxxx')
alls = list(set(alls))
for i in alls:
    print(i)
    print('______')