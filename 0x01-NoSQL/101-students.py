#!/usr/bin/env python3
from pymongo import MongoClient

def top_students(mongo_collection):
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$name", "average_score": {"$avg": "$topics.score"}}},
        {"$sort": {"average_score": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    my_db = client.my_db
    students_collection = my_db.students

    top_students_list = top_students(students_collection)
    for student in top_students_list:
        print(student)
