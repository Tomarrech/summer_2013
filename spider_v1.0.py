__author__ = 'issahar'
import db_module, xml_downloader

while True:
    print "Chose what you want to do:\n\t1)download all files\n" \
          "\t2)update db\n\t3)search by ib in db\n\t4)clear db\n\t5)exit"
    key = input('\=> ')
    if key == 1:
        xml_downloader.all_download()
    if key == 2:
        break
    if key == 3:
        db_module.search()
    if key == 4:
        break
    if key == 5:
        exit('bye')
