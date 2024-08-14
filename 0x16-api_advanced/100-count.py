#!/usr/bin/python3
"""
doc
"""
import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """
    Recursively queries the Reddit API and counts the occurrences
    of keywords in the titles of hot articles.

    Args:
    subreddit (str): The name of the subreddit to query.
    word_list (list): A list of keywords to count.
    after (str): The 'after' parameter for pagination (used for recursion).

    Returns:
    None: Prints the sorted keyword counts.
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

            # Collect titles
            titles = [child["data"].get("title", "") for child in children]

            # Create a Counter to keep track of keyword occurrences
            word_counter = Counter()

            # Process each title
            for title in titles:
                # Normalize title to lowercase
                title = title.lower()
                # Remove non-alphanumeric characters except spaces
                title = re.sub(r'[^a-z0-9\s]', '', title)
                # Split the title into words
                words = title.split()
                # Count occurrences of each keyword
                for word in word_list:
                    word_counter[word] += words.count(word.lower())

            # Recursively get the next page
            if new_after:
                return count_words(subreddit, word_list, after=new_after)
            else:
                # Sort and print results
                sorted_words = sorted(
                    word_counter.items(),
                    key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")

        else:
            # Invalid subreddit or other error
            return

    except requests.RequestException:
        # Handle request errors
        return
