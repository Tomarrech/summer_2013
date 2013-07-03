#coding: utf8
__author__ = 'Tomarrech'
import lxml.html
import urllib2, urllib
import cookielib

cookie = cookielib.CookieJar()
req = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
req.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'), ]
resp = req.open('https://login.vk.com/?act=login', urllib.urlencode({'email': '89281118476', 'pass': '28zrw35q'}))

page = req.open('https://vk.com/id216378560').read().decode('cp1251')

xmldata = lxml.html.document_fromstring(page)
UserName = xmldata.xpath('//div[@class="page_name fl_l ta_l"]/text()')
UserStatus = xmldata.xpath('//span[@class="current_text"]/text()')

#UserCity = xmldata.xpath('//div[@href="/search?c[name]=0&c[section]=people&c[hometown]="]/text()')
tree = lxml.etree.HTML(page)
print tree.xpath('/html/body/div[11]/div/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/a')
print "name is ", UserName[0]
print '\nstatus is: ', UserStatus[0]
print '\ncity is '
print "END!"

