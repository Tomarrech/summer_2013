__author__ = 'issahar'
import urllib2
import time
import re
from bs4 import BeautifulSoup
from BS_parsing import Parsing


def all_download():
    prime_link = 'http://nvd.nist.gov/download.cfm'
    page = urllib2.urlopen(prime_link)
    soup = BeautifulSoup(page)
    reg = re.compile('http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-.*')
    entries = soup.findAll('a', href=reg)
    time1 = time.time()
    for entry in entries:
        link = "http://static.nvd.nist.gov/feeds/xml/cve/"+entry.string
        print "\n", link
        xml = urllib2.urlopen(link)
        Parsing(entry.string, xml, 'vuln:cve-id', 'vuln:product', 'vuln:summary', 'vuln:published-datetime')
    print '\n\nparsing complited for', time.time()-time1, 'sec'