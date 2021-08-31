from pymongo import MongoClient
from bson.json_util import dumps, loads
  

def get_json(client,file_name,collection):
    mydatabase = client['COMPANY']
    mycollection = mydatabase[collection]
    cursor = mycollection.find()
    # list_cur = list(cursor)
    json_data = dumps(cursor, indent = 2) 

    file_name = 'JSON_FILES/'+file_name
    with open(file_name, 'w') as file:
        file.write(json_data)
    print(file_name+" Created")