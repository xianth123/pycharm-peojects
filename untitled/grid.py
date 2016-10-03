import pymongo
from gridfs import *

client = pymongo.MongoClient('localhost', 27017)
db = client['db']
fs = GridFS(db, 'geids')

for i in range(400):
    fs.put('quyeuyqi iuh')