__author__ = 'Issahar'
import MySQLdb


def db_create(db_name):
    """

    :param db_name
    """
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="nvd", charset="utf8")
    cursor = db.cursor()
    query = 'CREATE TABLE IF NOT EXISTS '+db_name+'' \
        ' (id LONGTEXT, products LONGTEXT, summary LONGTEXT, datetime LONGTEXT)'
    q = 'SHOW TABLES FROM nvd LIKE "'+db_name+'"'

    if not cursor.execute(q):
        print "creating..."
        cursor.execute(query)
    else:
        print "db", db_name, 'already exist\n'
    db.commit()
    db.close()


def db_insert(db_name, cid, prod, summ, dtime):
    """


    :param db_name:
    :param cid:
    :param prod:
    :param summ:
    :param dtime:
    """
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="nvd", charset="utf8")
    cursor = db.cursor()
    query = "INSERT INTO "+db_name+" (id, products, summary, datetime) VALUES " \
                                   "('%s','%s','%s','%s')" % (cid, prod, summ, dtime)
    cursor.execute(query)

    db.commit()
    db.close()


def search():
    """


    """
    print 'searching...'
#TODO in list of tables search for each element
    print "search complited..."