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

sql_gas = "INSERT INTO GAS(topic,payload) VALUES(%s,%s)"
sql_dust = "INSERT INTO DUST(topic,payload) VALUES(%s,%s)"
sql_illum = "INSERT INTO ILLUMINANCE(topic,payload) VALUES(%s,%s)"
sql_pir = "INSERT INTO PIR(topic,payload) VALUES(%s,%s)"
sql_temp = "INSERT INTO TEMP(topic,payload_t,payload_h) VALUES(%s,%s,%s)"

def insert_gas():
    
    for i in range(0,5):
        cur.execute(sql_gas, ('gas', str(i)))
        db.commit()
        time.sleep(5)
        
def insert_dust():
    
    for i in range(0,5):
        cur.execute(sql_dust, ('dust', str(i)))
        db.commit()
        time.sleep(5)
        
def insert_ill():
    
    for i in range(0,5):
        cur.execute(sql_illum, ('illum', str(i)))
        db.commit()
        time.sleep(5)
        
def insert_pir():
    
    for i in range(0,2):
        cur.execute(sql_gas, ('pir', str(i)))
        db.commit()
        time.sleep(5)
        
def insert_temp():
    
   for i in range(0,5): 
    for j in range(5,10):
        cur.execute(sql_temp, ('gas', str(i), str(j)))
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
            insert_temp()

            
    except:
        exit()        
     

          

