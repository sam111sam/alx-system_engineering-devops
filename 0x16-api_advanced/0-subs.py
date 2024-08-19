#!/usr/bin/python3
"""Function to fetch the number of subscribers for a specified Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Fetch and return the total subscriber count for the specified subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "custom:api.query:v1.0.0 (by /u/your_username)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 404:
        return 0
    
    data = response.json().get("data")
    return data.get("subscribers")

