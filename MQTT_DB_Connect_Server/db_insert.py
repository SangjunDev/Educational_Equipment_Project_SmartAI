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
    
    for i in range(10000):
        cur.execute(insert_sql, ('gas', str(i)))
        db.commit()
        time.sleep(5)
    

def db_truncate():
    sql = "TRUNCATE GAS;"
    cur.execute(sql)
    db.commit()
    
if __name__ == '__main__':
    
    try:
        while True:
            atexit.register(db_truncate)
            insert_db()
    except:
        exit()        
     

          

