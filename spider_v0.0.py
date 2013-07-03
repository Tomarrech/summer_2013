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
Uname = xmldata.xpath('//div[@class="page_name fl_l ta_l"]/text()')

print 'name is %s', Uname[0]





