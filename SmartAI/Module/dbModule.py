#import pymysql
import mariadb


class Database():
    def __init__(self):
     self.db = mariadb.connect(host='127.0.0.1',
                                  user='root',
                                  password='1234qwer',
                                  db='SmartAI')
                                  #,charset='utf8')     
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
        
