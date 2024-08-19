#!/usr/bin/python3
"""Function to retrieve the subscriber count for a specific Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Fetch and return the total number of subscribers for the provided subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Immediate-Piano3234)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

