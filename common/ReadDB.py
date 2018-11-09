import pymssql
import ReadConfig 


class Pymssql:
    def __init__(self,):
        readconfig=ReadConfig.ReadConfig()
        DBIp = readconfig.get_db('ip')
        DBUserName = readconfig.get_db('username')
        DBPassWord = readconfig.get_db('password')
        DBName= readconfig.get_db('dbname')
        self.conn = pymssql.connect(DBIp,DBUserName,DBPassWord,DBName)
        self.cursor = self.conn.cursor()
        
    def GetSmsDate(self):
        sql = "SELECT * FROM [dbo].[SmsRecord]"
        self.cursor.execute(sql)
        print(self.cursor.fetchone()[4])
        
