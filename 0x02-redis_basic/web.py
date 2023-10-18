import requests
import redis

# Create a Redis client
redis_client = redis.Redis()

def get_page(url: str) -> str:
    # Generate the key for counting accesses
    count_key = f"count:{url}"
    
    # Check if the URL content is cached
    cached_response = redis_client.get(url)

    if cached_response:
        # If cached, increment the access count and return the cached content
        redis_client.incr(count_key)
        return cached_response.decode('utf-8')
    else:
        # If not cached, make an HTTP request to the URL
        response = requests.get(url)

        if response.status_code == 200:
            # Cache the response with a 10-second expiration
            redis_client.setex(url, 10, response.text)
            
            # Initialize the access count to 1 for a new URL
            redis_client.set(count_key, 1)
            
            return response.text
        else:
            return f"Failed to retrieve the page. Status code: {response.status_code}"

if __name__ == "__main__":
    # URL to retrieve
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://example.com"
    page_content = get_page(url)
    
    # Get the access count
    access_count = redis_client.get(f"count:{url}").decode('utf-8')
    
    print(f"Page content:\n{page_content}")
    print(f"Access count: {access_count}")
