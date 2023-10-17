#!/usr/bin/env python3
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    my_db = client.my_db
    school_collection = my_db.school

    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created:", new_school_id)
