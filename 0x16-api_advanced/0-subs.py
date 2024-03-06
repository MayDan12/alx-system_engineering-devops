#!/usr/bin/python3
'''
  the function number_of_subscribers in reddit
'''
import requests


def number_of_subscribers(subreddit):
    '''
        This methods returns the number of subscribers for a given subreddit
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")