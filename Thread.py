#! usr/bin/python
#coding=utf-8
import urllib2
import thread
import random
def download():
    i = random.randint(11, 14)
    # print str(i)
    send_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
    }
    proxy = urllib2.ProxyHandler({'http': 'http://user' + str(i) + ':123@192.168.0.99:3128'})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    conn = urllib2.urlopen("http://www.speedtest.cn/")
    conn.read()

'''for i in range(100):
 try:
     thread.start_new_thread(download,())
 except:
    print "Error: unable to start thread"
    pass
while 1:
 pass'''
download()