from pymongo import MongoClient

client = MongoClient("mongodb+srv://ganeshbabumadhavan:Babu7181@babudb.rc7jj7n.mongodb.net/")

db = client["CST"]

collection = db["Students"]

# Inserting 
collection.insert_many([
    {"_id":101,"Name":"Babu", "Age":21,},
    {"_id":102,"Name":"Bala","Age":16},
    {"_id":103,"Name":"Arun","Age":22}
])
print("\n\n-------------Inserted Successful!!-------------\n\n")

# READ - reading
for i in collection.find():
    print(i)

# UPDATE 

collection.update_one(
    { "Name":"Arun"},
    {"$set":{"Age":25}}
)
print("\n-----------------Update successfull--------------------\n")
for i in collection.find():
    print(i)

# DELETE 
collection.delete_one(
    {
        "Name":"Arun"
    }
)
print("\n-----------------Deleted successfull--------------------\n")
for i in collection.find():
    print(i)