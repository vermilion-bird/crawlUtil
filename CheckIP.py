#!/usr/bin/python
# -*- coding: utf-8 -*-
#检查ip能否ping通
#0:正常，1：ping不通
import random
import urllib2
import subprocess
import re
import time
from lxml import html
from bs4 import BeautifulSoup
from lxml import etree
import random

from proxySql import proxySql

proxySql = proxySql()
ipSet = set()
proxyObj = {}


def get_proxy_list(url):
    apiData = urllib2.urlopen(url)
    apiDic = eval(apiData.read())
    return apiDic

def check_ip_ping():
    apiDic = get_proxy_list("http://220.180.227.52:45654/getiplist")
    print  apiDic
    for addressObj in apiDic:
        p=subprocess.Popen([r'./ping.sh', addressObj['ip']], stdout=subprocess.PIPE)
        result = p.stdout.read()
        if result !='1\n' :
            print addressObj['ip'] +'Success!'
            check_ip_request(addressObj['ip'],11,30)
        else:
            print addressObj['ip']+'faild'
        pass

def get_ip_check_request():
    apiData = urllib2.urlopen("http://220.180.227.52:45654/getiplist")
    apiDic = eval(apiData.read())
    for addressObj in apiDic:
        check_ip_request(addressObj['ip'],11,12)


def check_ip_request(proxyIP,startID,endID):
 proxyObj['proxyIp'] = proxyIP
 ipList = []
 #proxyIP ='223.240.252.153'
 for i in range(startID,endID):
    #i = random.randint(11, 20)
   # print 'user'+str(i)
    startTime = time.time()
    proxy = urllib2.ProxyHandler({'http': 'http://user' + str(i) + ':123@'+proxyIP+':3128'})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    ipAddress=urllib2.urlopen("http://1212.ip138.com/ic.asp")
    content = ipAddress.read().decode('gb2312').encode('utf-8')
    length =time.time()-startTime;
    ip = content[content.index('[')+1:content.index(']')]
    ipobj = {}
    ipobj['user']='user'+str(i)
    ipobj['ip']=ip
    ipobj['timeInterval']=length
    if ip in ipSet:
        print '重复'
    ipSet.add(ip)
    #print ipSet
    #print len(ipSet)
   # print ('---------------------')
   # print (ipobj)
    ipList.append(ipobj)
    proxyObj['ipobj']=ipList
 print proxyObj
 pass
def check_ip_no_auth(proxy_info):
 #try:
    # We create a handler for the proxy
    proxy_support = urllib2.ProxyHandler({"http": "http://"+proxy_info[0]+':'+str(proxy_info[1])})
    # We create an opener which uses this handler:
    opener = urllib2.build_opener(proxy_support)
    # Then we install this opener as the default opener for urllib2:
    urllib2.install_opener(opener)
    startTime = time.time()
    ipAddress=urllib2.urlopen("http://1212.ip138.com/ic.asp")
    content = ipAddress.read().decode('gb2312').encode('utf-8')
    length = time.time() - startTime;
    ip = content[content.index('[') + 1:content.index(']')]
    ipobj = {}
    ipobj['ip'] = ip
    ipobj['timeInterval'] = length
    print ipobj

'''
for i in range(1,2):
    pass
    listIp = ['192.168.0.70','192.168.0.71','192.168.0.72','192.168.0.73','192.168.0.74','192.168.0.75','192.168.0.76','192.168.0.77']
    random.shuffle(listIp)
    for ip in listIp:
    #ip=listIp[random.randint(0,7)]
        print 'proxy========'+ip+'=============='
        check_ip_request(ip,11,13)


'''
#check_ip_ping()
#get_ip_check_request()
# proxyList = get_proxy_list("http://192.168.0.37:8000")
# for proxy in proxyList :
#     #proxySql.db_init()
#     #proxySql.insert_data(proxy)
#     print proxy
#     try:
#         check_ip_no_auth(proxy)
#     except:
#         continue

#get_ip_check_request()
#dic = get_proxy_list('http://220.180.227.52:45654/getiplist')
#for obj in dic:
check_ip_request('223.240.255.168',11,30)