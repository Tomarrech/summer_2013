__author__ = 'issahar'
from bs4 import BeautifulSoup
import db_module as db


class Parsing:

    def __init__(self, db_name, ffile, first_par, second_par, third_par, fourth_par):
        self.db_name = db_name
        self.ffile = ffile
        self.first_par = first_par
        self.second_par = second_par
        self.third_par = third_par
        self.fourth_par = fourth_par
        t = db_name.split('-')
        db_name = 'b_'+t[2][:-4]
        db.db_create(db_name)
        a = {'first': None, 'second': None, 'third': None, 'fourth': None}

        soup = BeautifulSoup(ffile)
        entries = soup.findAll('entry')
        for i in entries:
            a['second'] = 'versions:'
            for k in i.findAll(first_par):
                a['first'] = k.string
            for k in i.findAll(second_par):
                a['second'] += '\n'+k.string
            for k in i.findAll(third_par):
                a['third'] = k.string
            for k in i.findAll(fourth_par):
                a['fourth'] = k.string
            try:
                db.db_insert(db_name, a['first'], a['second'], a['third'], a['fourth'])
            except:
                print "\nERROR with", a['first'], ' sorry =( '
#TODO check, why some CVE's weren't add (smt with time)