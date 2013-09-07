__author__ = 'issahar'
from bs4 import BeautifulSoup


class Parsing:

    def __init__(self, file, first_par, second_par, third_par):
        self.file = file
        self.first_par = first_par
        self.second_par = second_par
        self.third_par = third_par

        soup = BeautifulSoup(file)
        entries = soup.findAll('entry')
        for i in entries:
            for k in i.findAll(first_par):
                a = k.string
            for k in i.findAll(second_par):
                a = k.string
            for k in i.findAll(third_par):
                a = k.string

    def __str__(self):
        return "'%s', '%s' and '%s'" % (self.first_par, self.second_par, self.third_par)