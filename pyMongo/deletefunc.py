import pymongo as py
myClient = py.MongoClient("mongodb://localhost:27017/")
mydb = myClient["mydatabase"]
mycol = mydb["mycollection"]

deleteq = mycol.delete_many({"name":"Viola","address":"Valley 345"})
#deleteq = mycol.delete_many({"name":"Minnie"})
for z in mycol.find():
    print(z)