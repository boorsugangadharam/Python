import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['python_IOT']
dblist=myclient.list_database_names()
if "python_IOT" in dblist:
    print ("database exists. dbname: python_IOT")
else:
    pass
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

collist = mydb.list_collection_names()
print(collist)
if "customers" in collist:
    print("The collection exists.")