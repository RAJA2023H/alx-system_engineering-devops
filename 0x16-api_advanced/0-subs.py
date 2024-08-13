import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a specified subreddit
    using the Reddit API.
    Args:
    subreddit (str): The name of the subreddit to
    get the subscriber count from.
    Returns:
    int: The number of subscribers for the subreddit,
    or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Reddit-API-Query"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return (data["data"]["subscribers"])
        else:
            return (0)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return (0)
