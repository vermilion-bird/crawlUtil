#! usr/bin/python
#coding=utf-8
import urllib2
import random
import time
import threading
class Proxy(threading.Thread):
        timeList = []
        def __init__(self,lock):
         self.lock = lock  # 传入的lock对象
         pass
        def run(self):
         #self.lock.acquire()  # 获得lock对象，lock状态变为locked，并且阻塞其他线程获取lock对象（写文件的权利）
         self.testGe()
         #self.lock.release()  # 释放lock对象，lock状态变为unlocked，其他的线程可以重新获取lock对象

        def testGe(self):
         i=random.randint(11,14)
         print str(i)
         send_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive',
        }
         proxy = urllib2.ProxyHandler({'http': 'http://user'+str(i)+':1203@192.168.0.99:3128'})
        #proxy = urllib2.ProxyHandler({'http': 'http://192.168.0.91:3128'})
         auth = urllib2.HTTPBasicAuthHandler()
         opener = urllib2.build_opener(proxy,auth, urllib2.HTTPHandler)
         urllib2.install_opener(opener)
         #req = urllib2.Request("http://blog.csdn.net/jeanphorn/article/details/45195339", headers=send_headers)
         for i in range(10):
          #self.lock.acquire()  # 获得lock对象，lock状态变为locked，并且阻塞其他线程获取lock对象（写文件的权利）
          print "&&&&&"
          start = time.time()
          conn = urllib2.urlopen("http://www.xitongzhijia.net/win10/201707/102388.html")
          print conn.info();
          conn.read()

          cost=time.time()-start
          print "="+str(cost)+"="
         # self.lock.release()  # 释放lock对象，lock状态变为unlocked，其他的线程可以重新获取lock对象

         #self.timeList.append(cost)
         #print "time lose"+str(cost)
         #print conn.info
         #return_str = conn.read()
         #print conn.headers
         #print return_str.decode('gb2312').encode('utf-8')
         #print return_str.decode('utf-8')
         #proxy.close()
        def creatThread(self):
         # 创建两个线程
         try:
          for i in range(10):
           pass
           #thread.start_new_thread(self.testGe, ())
         except:
                print "Error: unable to start thread"
                pass
#instace=Proxy()
#instace.creatThread()
#instace.testGe()
lock = threading.Lock()
for i in range(100):
 Proxy(lock).run()
while 1:
 pass