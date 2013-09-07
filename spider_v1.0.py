__author__ = 'Tomarrech'
#http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-recent.xml
import urllib2, urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('nvdcve-2.0-recent.xml'))
entries = soup.findAll('entry')

for i in entries:
    for k in i.findAll('vuln:cve-id'):
        print 'name: ',k.string
    for k in i.findAll('vuln:reference'):
        print "reference: ",k.string
    for k in i.findAll('vuln:summary'):
        print "summary: ",k.string