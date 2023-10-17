#!/usr/bin/env python3
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return result.modified_count

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    my_db = client.my_db
    school_collection = my_db.school

    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])
    update_topics(school_collection, "Holberton school", ["iOS"])
