import requests
import time

headers = {
    "user-agent": "Mozilla/5.0"
}

def get_user_data(username):
    url = f"https://onlyfans.com/api2/v2/users/{username}"
    
    try:
        res = requests.get(url, headers=headers)
        data = res.json()
        
        price = data.get("subscribePrice")
        posts = data.get("postsCount")
        last_seen = data.get("lastSeen")
        
        return {
            "username": username,
            "price": price,
            "posts": posts,
            "last_seen": last_seen
        }
    except:
        return {
            "username": username,
            "price": None,
            "posts": None,
            "last_seen": None
        }

with open("users.txt") as f:
    users = f.read().splitlines()

for user in users:
    result = get_user_data(user)
    print(result)
    time.sleep(2)
