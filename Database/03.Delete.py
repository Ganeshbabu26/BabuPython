from pymongo import MongoClient

client = MongoClient("mongodb+srv://ganeshbabumadhavan:Babu7181@babudb.rc7jj7n.mongodb.net/")

db = client["MyMongoDb"]

collection = db["Students"]

collection.insert_one(
    {
        "Name":"Arun",
        "Age":22
    }
)
print("Inserted successful!")

print("\n\n----------------------------------------------\n\n")
for i in collection.find():
    print(i)

print("\n\n----------------------------------------------\n\n")
collection.update_one(
    {
        "Name":"Arun"
    },
    {
        "$set":{"Age":25}
    }
)

for i in collection.find():
    print(i)

print("\n\n----------------------------------------------\n\n")
collection.delete_one(
    {
        "Name":"Arun"
    }
)

print("\n\n----------------------------------------------\n\n")

print("deleted successful")

for i in collection.find():
    print(i)