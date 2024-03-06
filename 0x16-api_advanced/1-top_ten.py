#!/usr/bin/python3
'''
    This function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        This method returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    urls = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for posts in urls.get('data').get('children'):
            print(posts.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])