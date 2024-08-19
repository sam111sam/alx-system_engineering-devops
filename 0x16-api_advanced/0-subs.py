#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "my_reddit_app/1.0 (by /u/Immediate-Piano3234)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 404:
        return 0
    elif response.status_code != 200:
        ''' print("Unexpected status code: {}".format(response.status_code))'''
        return 0
    
    # Ensure response encoding is correct
    response.encoding = 'utf-8'
    
    try:
        data = response.json().get("data")
        return data.get("subscribers")
    except ValueError:
        print("Failed to decode JSON from response.")
        return 0

