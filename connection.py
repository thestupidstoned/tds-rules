# importing module 
from pymongo import MongoClient 
  

try: 
   # creation of MongoClient 
    client=MongoClient() 
# Connect with the portnumber and host 
    client = MongoClient("mongodb://localhost:27017/")  
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
# Name of the databse 
mydb = client["mongoPythonDemo"] 
# Name of the collection 
mycol = mydb["mp1"] 
for items in mycol.find():
    print(items)