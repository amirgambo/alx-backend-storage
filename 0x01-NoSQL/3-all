#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    return list(mongo_collection.find())

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    my_db = client.my_db
    school_collection = my_db.school

    documents = list_all(school_collection)
    for doc in documents:
        print(doc)
