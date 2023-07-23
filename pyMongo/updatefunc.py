import pymongo as py

myClient = py.MongoClient("mongodb://localhost:27017/")
mydb = myClient["mydatabase"]
mycol = mydb["mycollection"]

#query = {"address": "Valley 345"}
#update = {"$set": {"address": "Ghaati 346"}}
query = { "address": { "$regex": "1$" } }
update = { "$set": { "name": "Minnie" } }

mycol.update_many(query,update)

for x in mycol.find():
    print(x)