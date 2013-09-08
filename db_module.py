__author__ = 'Issahar'
import MySQLdb


def db_insert(cid, prod, summ, dtime):
    """

    :param cid:
    :param prod:
    :param summ:
    :param dtime:
    """
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="nvd", charset='utf8')
    cursor = db.cursor()
    cursor.execute("INSERT INTO nvd (id, products, summary, datetime) "
                   "VALUES ('%s','%s','%s','%s')" % (cid, prod, summ, dtime))

    db.commit()
    db.close()