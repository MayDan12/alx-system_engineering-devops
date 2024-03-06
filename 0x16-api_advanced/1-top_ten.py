#!/usr/bin/python3
'''
    This function top_ten
'''
import requests


def top_ten(subreddit):
    '''
        This method returns the top ten posts for a given subreddit
    '''
    
    urls ='https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    params = {
        'limit': 10
    }
    response = requests.get(urls, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    result = response.json().get("data")
    [print(c.get("data").get("title")) for c in result.get("children")]
