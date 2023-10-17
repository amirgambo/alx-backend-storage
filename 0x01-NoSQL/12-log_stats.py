#!/usr/bin/env python3
from pymongo import MongoClient

def log_stats(mongo_collection):
    count = mongo_collection.count_documents({})
    methods = {
        "method GET": mongo_collection.count_documents({"method": "GET"}),
        "method POST": mongo_collection.count_documents({"method": "POST"}),
        "method PUT": mongo_collection.count_documents({"method": "PUT"}),
        "method PATCH": mongo_collection.count_documents({"method": "PATCH"}),
        "method DELETE": mongo_collection.count_documents({"method": "DELETE"})
    }

    ip_counts = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print(count, "logs")
    print("Methods:")
    for method, count in methods.items():
        print(f"    {method}: {count}")
    print("IPs:")
    for ip_count in ip_counts:
        print(f"    {ip_count['_id']}: {ip_count['count']}")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx

    log_stats(nginx_collection)
