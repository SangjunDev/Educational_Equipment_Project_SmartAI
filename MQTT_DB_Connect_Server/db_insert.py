import pymysql
import time
import atexit

db = pymysql.connect(
    host='localhost',
    port=3306, 
    user='root', 
    passwd='1234qwer',
    db='SmartAI',
    charset='utf8')

cur = db.cursor()

insert_sql = "INSERT INTO GAS(topic,payload) VALUES(%s,%s)"

def insert_db():
    cur.execute(insert_sql, ('gas', '2'))
    db.commit()
    time.sleep(3)
    cur.execute(insert_sql, ('gas', '3'))
    db.commit()
    


def db_truncate():
    sql = "TRUNCATE GAS;"
    cur.execute(sql)
    db.commit()
    
if __name__ == '__main__':
    
    try:
        while True:
            atexit.register(db_truncate)
            insert_db()
            time.sleep(5)
    except:
        exit()        
     

          

