import pymysql
from DBUtils.PooledDB import PooledDB

 
MYSQL_HOST = 'localhost'
USER = 'root'
PASSWORD = '12345678'
DB = 'cnu'
PORT = 3306

pool = PooledDB(pymysql, 5, host=MYSQL_HOST, user=USER, passwd=PASSWORD, db=DB, port=PORT) 

con = pool.connection()

def main():
    a = ['asde', 'aesd', 'ased', 'ased', 'aesd', 'aesd', 'ased']
    # con = pymysql.connect(host='localhost', port=3306,
    #                       database='cnu', charset='utf8',
    #                       user='root', password='12345678')
    

    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'insert into works values (%s, %s, %s, %s, %s, %s, %s)',
                (a[0], a[1], a[2], a[3], a[4], a[5], a[6])
            )
        if result == 1:
            print('success')
        con.commit()
    finally:
        con.close()

if __name__ == "__main__":
    main()