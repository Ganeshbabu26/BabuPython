from pymongo import MongoClient

client = MongoClient("mongodb+srv://ganeshbabumadhavan:Babu7181@babudb.rc7jj7n.mongodb.net/")

db = client["MyMongoDb"]

collection = db["Students"]

collection.insert_one(
    {
        "Name":"Babu",
        "Age":21
    }
)

collection.insert_one(
    {
        "Name":"Bala",
        "Age":16
    }
)

print("Inserted successfully")


for i in collection.find():
    print(i)