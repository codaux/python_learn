import requests
import re
import base64

headers = {
  'User-Agent':
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
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
  'https://t.me/s/FalconPolV2rayNG',
  'https://t.me/s/PrivateVPNs',
  'https://t.me/s/MehradLearn',
  'https://t.me/s/v2rayNGN',
  'https://t.me/s/hashmakvpn',
  'https://t.me/s/v2rayNGN',
]
chann64 = [
'https://raw.githubusercontent.com/ssrsub/ssr/master/trojan',
'https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray',
'https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub',
'https://raw.githubusercontent.com/clashconfig/UFO/main/UFO_base.txt',
'https://raw.githubusercontent.com/rezasamaniiii/ss/main/ss.txt',
'https://git.io/darkb'
]
all = []
def ex(c):
  vmess = re.findall('>(vmess:.+?)[<]', c)
  vless = re.findall('>(vless:.+?)[<]', c)
  ss = re.findall('>(ss:.+?)[<]', c)
  trojan = re.findall('>(trojan:.+?)[<]', c)
  sn = re.findall('>(sn:.+?)[<]', c)
  xray = re.findall('>(xray:.+?)[<]', c)
  wireguard = re.findall('>(wireguard:.+?)[<]', c)
  ex = vmess + vless + ss + trojan + sn + xray + wireguard
  return ex

#p = { 'socks5' : '127.0.0.1:10808' }
for x in chann:
  c = requests.get(x, headers=headers).text
  d = ex(c)
  all = all + d

for x in chann64:
  w = requests.get(x, headers=headers).text
  w = str(base64.b64decode(w),'utf-8')
  wx = w.splitlines()
  all = all + wx

all = list(set(all))

with open('ss.txt', 'w') as f:
    f.write(str(all))

with open('your_file.txt', 'w') as f:
    for line in all:
        f.write(f"{line}\n")