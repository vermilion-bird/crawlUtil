#!/usr/bin/python
# -*- coding: utf-8 -*-
#检查ip能否ping通
#0:正常，1：ping不通
import random
import urllib2
import subprocess
import re

def check_ip_ping():
    apiData = urllib2.urlopen("http://220.180.227.52:45654/getiplist")
    apiDic = eval(apiData.read())
    print  apiDic
    for addressObj in apiDic:
        p=subprocess.Popen([r'./ping.sh', addressObj['ip']], stdout=subprocess.PIPE)
        result = p.stdout.read()
        if result !='1\n' :
            print addressObj['ip'] +'Success!'
        else:
            print addressObj['ip']+'faild'
        pass

def check_ip_request():
 for i in range(11,20):
    #i = random.randint(11, 20)
    print i
    proxy = urllib2.ProxyHandler({'http': 'http://user' + str(i) + ':123@192.168.0.90:3128'})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    ipAddress=urllib2.urlopen("http://1212.ip138.com/ic.asp")
    #content = ipAddress.read().decode('gb2312').encode('utf-8')
#    ipStr = re.search('<center>',content)
  #  print ipStr.string
    print ipAddress.read().decode('gb2312').encode('utf-8')

    pass

for i in range(1,2):
    pass
    check_ip_request()

#check_ip_ping()