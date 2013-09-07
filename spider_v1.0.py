__author__ = 'Tomarrech'
#http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-recent.xml
import urllib2
import time
from BS_parsing import Parsing

file = urllib2.urlopen('http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2003.xml')

time1 = time.time()
ara = Parsing(file, 'vuln:cve-id', 'vuln:reference', 'vuln:summary')

print '\n\nparsing complited for', time.time()-time1, 'sec'