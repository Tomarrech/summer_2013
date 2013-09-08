__author__ = 'issahar'
import urllib2
import time
from BS_parsing import Parsing

link = 'http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-recent.xml'
xml = urllib2.urlopen(link)
time1 = time.time()
Parsing(xml, 'vuln:cve-id', 'vuln:product', 'vuln:summary', 'vuln:published-datetime')

print '\n\nparsing complited for', time.time()-time1, 'sec'



