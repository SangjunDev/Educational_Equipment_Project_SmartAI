import pymysql 
import time

    

def live_gas():
    db = pymysql.connect(host='localhost', 
                     port=3306, user='root', 
                     passwd='1234qwer', 
                     db='SmartAI', 
                     charset='utf8')
    
    
    cursor = db.cursor()
    sql_1 = " SELECT payload FROM GAS ORDER BY real_t DESC LIMIT 1"
    cursor.execute(sql_1)
    data = cursor.fetchall() 
    print(data)
    #data = json.dumps(cursor.fetchall())
    
    return data

if __name__ == '__main__':
    while True:
        live_gas()
        time.sleep(3)
        