import pymongo as py
myClient = py.MongoClient("mongodb://localhost:27017/")
mydb = myClient["mydatabase"]
mycol = mydb["mycollection"]

print(mycol.find_one())

for z in mycol.find():
    print(z)

for z in mycol.find({},{'name': 'vicky'}):
    print(z)

for z in mycol.find({},{'_id':0, 'name': 1,'address':1}):
    print(z)

for z in mycol.find({},{'_id':0,'address':0}):
    print(z)
# 0 means exclude, 1 means include

