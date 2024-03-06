#!/usr/bin/python3
"""This function query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
  """
    This method returns a list of titles of all hot posts on  given subreddit.
  """
  urls = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
  headers = {
     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
  }
  param = {
    "after": after,
    "count": count,
    "limit": 100
  }

  response = requests.get(urls, headers=headers, param=param, allow_redirects=False)
  if response.status_code == 404:
    return None
  
  result = response.json().get("data")
  after = result.get("after")
  count += result.get("dist")
  for d in result.get("children"):
    hot_list.append(d.get("data").get("title"))

  if after is not None:
    return recurse(subreddit, hot_list, after, count)
  return hot_list