#!/usr/bin/env python3
from pymongo import MongoClient

def log_stats(mongo_collection):
    # Calculate the total number of logs
    total_logs = mongo_collection.count_documents({})

    # Calculate the number of logs for each method
    methods = mongo_collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ])
    method_stats = {method["_id"]: method["count"] for method in methods}

    # Calculate the number of logs with method=GET and path=/status
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    # Calculate the top 10 IPs
    top_ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    ip_stats = {ip["_id"]: ip["count"] for ip in top_ips}

    return total_logs, method_stats, status_check_count, ip_stats

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx

    total_logs, method_stats, status_check_count, ip_stats = log_stats(nginx_collection)

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_stats.items():
        print(f"    method {method}: {count}")

    print(f"{status_check_count} status check")
    print("IPs:")
    for ip, count in ip_stats.items():
        print(f"    {ip}: {count}")
