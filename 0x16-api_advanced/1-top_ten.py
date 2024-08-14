#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""

import requests

def top_ten(subreddit):
    """
    """
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
         data = response.json().get("data")
         posts = data.get("children", [])

         for i, post in enumerate(posts[:10]):
             print(f"{i+1}. {post['data']['title']}")
    else:
        print(None)
