#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API to retrieve the number of subscribers for a given subreddit.
    """

    urls = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "YourCustomUserAgent/1.0"}  # Set a custom User-Agent

    try:
        response = requests.get(urls, header=header, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-200 status codes

        data = response.json()
        return data.get("data", {}).get("subscribers")

    except requests.exceptions.RequestException:
        return 0

