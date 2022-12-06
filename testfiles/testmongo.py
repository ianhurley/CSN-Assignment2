import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://scanut:scanut@cluster0.x0cl6dg.mongodb.net/test")

db = cluster["test"]
collection = db["testing123"]

collection.insert_one({"_id":5, "user_name":"Orin"})
collection.insert_one({"_id":6, "user_name":"Hurley"})