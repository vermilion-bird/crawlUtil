import urllib2

url='http://www.126.com'
page=urllib2.urlopen('http://www.126.com')

user_agent=	"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"
header={'User_Agent':user_agent}
page=urllib2.Request(url,'',header)
print page.read()
print page.info
print page.geturl()
print page.getcode()