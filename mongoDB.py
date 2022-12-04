import pymongo
from pymongo import MongoClient

# connecting to MongoDB Atlas cloud database
cluster = MongoClient("mongodb+srv://scanut:scanut@cluster0.x0cl6dg.mongodb.net/test")

db = cluster["ScaNutDB"]
collection = db["confectionary"]

# inserting sample product containing nuts
collection.insert_one({"_id":5000159470629, "Name":"Snickers", "Size":"48g", "Ingredients":"Sugar, glucose syrup, peanuts, skimmed milk powder, cocoa butter, cocoa mass, sunflower oil, lactose, milk fat, whey powder (from milk), palm fat, salt, emulsifier (soya lecithin), egg white powder, milk protein, natural vanilla extract.","Allergens":"Eggs, Milk, Peanuts, Soybeans","May contain":"hazelnut"})

# inserting sample product that may contain traces
collection.insert_one({"_id":5034660004004, "Name":"Dairymilk", "Size":"53g", "Ingredients":"milk, sugar, cocoa butter, cocoa mass, vegetable fats (palm, shea), emulsifiers (e442, e476)","Allergens":"Milk","May contain":"gluten, nuts"})

# inserting sample product that do not contain nuts or traces
collection.insert_one({"_id":7613034872579, "Name":"Yorkie", "Size":"46g", "Ingredients":"sugar, dried whole milk, coco butter, cocoa mass, vegetable fats (palm, shea, mango kernel, sal), lactose and proteins from whey (from milk), whey powder (from milk), skimmed milk powder, butterfat (from milk), emulsifier (sunflower lecithin)","Allergens":"Milk","May contain":"gluten"})