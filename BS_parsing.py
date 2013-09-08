__author__ = 'issahar'
from bs4 import BeautifulSoup
import db_module as db


class Parsing:

    def __init__(self, ffile, first_par, second_par, third_par, fourth_par):
        self.ffile = ffile
        self.first_par = first_par
        self.second_par = second_par
        self.third_par = third_par
        self.fourth_par = fourth_par

        a = {'first': None, 'second': None, 'third': None, 'fourth': None}

        soup = BeautifulSoup(ffile)
        entries = soup.findAll('entry')
        for i in entries:
            a['second'] = 'versions:'
            for k in i.findAll(first_par):
                a['first'] = k.string
            for k in i.findAll(second_par):
                a['second'] += 'hui'+k.string
            for k in i.findAll(third_par):
                a['third'] = k.string
            for k in i.findAll(fourth_par):
                a['fourth'] = k.string
            try:
                db.db_insert(a['first'], a['second'], a['third'], a['fourth'])
            except:
                print "\nERROR with", a['first'], ' sorry =( '