from pymongo import MongoClient

# mongo_uri = "mongodb+srv://dbGDR:dbYahiaUsers@cluster-gdr.mongodb.net/mongodbVSCodePlaygroundDB?retryWrites=true&w=majority"
# mongo_uri = "mongodb+srv://dbGDR:dbYahiaUsers@cluster-gdr.mongodb.net/mongodbVSCodePlaygroundDB?retryWrites=true&w=majority"
# client = MongoClient(mongo_uri)
client = MongoClient(
      "mongodb+srv://dbGDR:dbYahiaUsers@cluster-gdr.yogka.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-GDR")
# client = MongoClient(mongo_uri)
db = client['mongodbVSCodePlaygroundDB']
collection = db['sales']
# List all databases
database_names = client.list_database_names()

# Test the connection
try:
    client.admin.command('ping')
    print("Databases in MongoDB:")
    for db_name in collection.find():
        print(db_name)
except Exception as e:
    print(f"Failed to connect: {e}")