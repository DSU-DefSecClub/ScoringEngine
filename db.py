import pymysql

def connect():
    connection = pymysql.connect(host='localhost', 
            user='root', password='Waterworld1!')
    return connection

def get(cmd, args=None):
    connection = connect()
    with connection.cursor() as cursor:
        cursor.execute('USE scoring')
        cursor.execute(cmd, args)
        rows = cursor.fetchall()
    connection.close()
    return rows

def execute(cmd, args=None):
    connection = connect()
    with connection.cursor() as cursor:
        cursor.execute('USE scoring')
        cursor.execute(cmd, args)
        lid = cursor.lastrowid
    connection.commit()
    connection.close()
    return lid
