#!/usr/bin/python3
"""
this doc for module
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to get all hot
    article titles from a given subreddit.

    Args:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): Accumulates the titles of hot articles
    (used for recursion).
    after (str): The 'after' parameter for pagination (used for recursion).

    Returns:
    list: A list containing the titles of all hot articles,
    or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    params = {"after": after} if after else {}

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )

        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            new_after = data.get("after")

            if not children:
                return hot_list if hot_list else None

            for child in children:
                title = child["data"].get("title")
                if title:
                    hot_list.append(title)

            if new_after:
                return recurse(subreddit, hot_list, after=new_after)
            else:
                return hot_list

        else:
            return None

    except requests.RequestException:
        return None
