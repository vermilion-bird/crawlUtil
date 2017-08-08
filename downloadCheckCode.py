# -*- coding: utf-8 -*-
import urllib2
from lxml import etree
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://ip.zdaye.com/')
for item in cookie:
 print item.value   
#html=urllib2.urlopen('http://ip.zdaye.com/').read().decode('gb2312')

#print(html)
#html=etree.HTML(html)

#img = html.xpath('//img')
#print img