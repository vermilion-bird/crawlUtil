import MySQLdb

class proxySql(object):
    dbUrl = '*'
    dbUser = '*'
    dbPwd = '*'
    dataName = '*'
    def db_init(self):
        self.db = MySQLdb.connect(self.dbUrl, self.dbUser, self.dbPwd, self.dataName)
        return self.db
    def insert_data(self,proxy):
     try:
        sql = 'INSERT INTO t_proxy_ip(proxy_ip,proxy_port)VALUES ("'+proxy[0]+'","'+str(proxy[1])+'")'
        cursor = self.db.cursor()
        cursor.execute(sql)
        pass
     except:
         pass
p=proxySql()
db=p.db_init()
p.insert_data([1,2])
