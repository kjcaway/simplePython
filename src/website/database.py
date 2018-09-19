from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.test

members = db.members

# test
print("members:")
for x in members.find():
  print(x)