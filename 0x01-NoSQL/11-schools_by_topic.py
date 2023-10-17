#!/usr/bin/env python3
from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    return list(mongo_collection.find({"topics": topic}))

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    my_db = client.my_db
    school_collection = my_db.school

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print(school)
