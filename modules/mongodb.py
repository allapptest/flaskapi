# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:06:54 2021

@author: Bishop
"""

class mongoProcess:
    def get_database():
        from pymongo import MongoClient
        import pymongo
    
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        #CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
        CONNECTION_STRING = "mongodb://localhost:27017/blogusers"
        # mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false
        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        from pymongo import MongoClient
        client = MongoClient(CONNECTION_STRING)
    
        # Create the database for our example (we will use the same database throughout the tutorial
        return client['blogusers']

if __name__ == "__main__":
    
    item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
    "category" : "kitchen appliance"
    }
    
    item_2 = {
    "_id" : "U1IT00002",
    "item_name" : "Egg",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "brown country eggs"
    }
    
    dbname =  mongoProcess.get_database()
    print(dbname)
    collection_name = dbname["blogusers"] # get the collection
    #collection_name = dbname["blogusers"]
    collection_name.insert_many([item_1,item_2])