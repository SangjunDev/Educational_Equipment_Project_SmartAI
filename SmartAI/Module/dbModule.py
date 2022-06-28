import pymysql

allSelect = { 'illuminace' : 'SELECT * FROM ILLUMINANCE',
        'gas': 'SELECT * FROM GAS',
        'temp': 'SELECT * FROM TEMP',
        'dust': 'SELECT * FROM DUST',
        'pir': 'SELECT * FROM PIR'
}

apiSql = { 'illuminace' : 'SELECT id,topic,payload,time(real_t) FROM ILLUMINANCE ORDER BY id DESC LIMIT 1',
        'gas': 'SELECT id,topic,payload,time(real_t) FROM GAS ORDER BY id DESC LIMIT 1',
        'temp': 'SELECT id,topic,payload_t,payload_h,time(real_t) FROM TEMP ORDER BY id DESC LIMIT 1',
        'dust': 'SELECT id,topic,payload,time(real_t) FROM DUST ORDER BY id DESC LIMIT 1',
        'pir': 'SELECT id,topic,payload,time(real_t) FROM PIR ORDER BY id DESC LIMIT 1'
}

socketSql = { 'illuminace' : 'SELECT payload,time(real_t) FROM ILLUMINANCE ORDER BY id DESC LIMIT 1',
        'gas': 'SELECT payload,time(real_t) FROM GAS ORDER BY id DESC LIMIT 1',
        'temp': 'SELECT payload_t,payload_h,time(real_t) FROM TEMP ORDER BY id DESC LIMIT 1',
        'dust': 'SELECT payload,time(real_t) FROM DUST ORDER BY id DESC LIMIT 1',
        'pir': 'SELECT payload,time(real_t) FROM PIR ORDER BY id DESC LIMIT 1'
}


class Database():
    def __init__(self):
     self.db = pymysql.connect(host='127.0.0.1',
                               port = 3306, 
                                  user='root',
                                  password='1234qwer',
                                  db='SmartAI',
                                  charset='utf8')
                                  #cursorclass=pymysql.cursors.DictCursor)   
                                    
     self.cursor = self.db.cursor()
        

    def execute(self, query, args={}):
        self.cursor.execute(query, args)  
 
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row
 
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row
        
    def commit(self):
        self.db.commit()
        
def raedData(query, args={}):
    db = Database()
    row = db.executeAll(query, args={})
    return row
    