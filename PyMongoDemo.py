import pymongo
from pymongo import MongoClient
class mongod:
    def get_client(self,dbAddr,port):
        client = MongoClient()
        client = MongoClient(dbAddr,port)
        uriClient = MongoClient('URI://'+dbAddr+':'+port+'/')
        return client
    def connect_db(self,dbname):
        client = self.get_client('127.0.0.1','27017')
        db = client.dbname
        db = client[dbname]
        return db
    def connet_collection(self,colname):
        db =self.connect_db('test_name')
        collection = db.colname
        collection = db[colname]
        return collection
    def insert_document(self,doc,is_one,collect):
        if is_one:
            objId = collect.insert_one(doc).inserted_id
        else:
            objId = collect.insert_many(doc).inserted_ids
        return objId
    def query(self,collection,conditon,is_one):
        if is_one:
            result = collection.find_one(conditon)
        else:
            result = collection.find(conditon)
        return result
    def count(self):
        pass
