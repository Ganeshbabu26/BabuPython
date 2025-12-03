from pymongo import MongoClient

client = MongoClient("mongodb+srv://ganeshbabumadhavan:Babu7181@babudb.rc7jj7n.mongodb.net/")

db = client["MyMongoDb"]

collection = db["Students"]


collection.update_one({"Name":"Bala"},{"$set":{"Name":"Balakumaran"}})
print("Updated successful!")


for i in collection.find():
    print(i)