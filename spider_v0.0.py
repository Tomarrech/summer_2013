#coding: utf8
__author__ = 'Tomarrech'
import lxml.html
import urllib2, urllib
import cookielib

cookie = cookielib.CookieJar()
req = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
req.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'), ]
resp = req.open('https://login.vk.com/?act=login', urllib.urlencode({'email': '89287664564', 'pass': '*********'}))

page = req.open('https://vk.com/issahar').read()
print page.decode('cp1251')
print '\n\tolololo'
"""
page = urllib.urlopen('http://vk.com/issahar/')
pageWritten = page.read()
print pageWritten

#pageReady = pageWritten.decode()

#xmldata = lxml.html.document_fromstring(pageReady)

#temperature = xmldata.xpath('//div[@class="b-thermometer__now"]/text()')
#clouds = xmldata.xpath('//div[@class="b-info-item b-info-item_type_fact-big"]/text()')

#print 'По данным Yandex сейчас в Москве %s, %s', temperature[0], clouds[0]
"""




