#!/usr/bin/python3
"""
Get titles of subreddit top 10 posts
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit,
    the function should return None
    """
    base_url = "https://www.reddit.com"
    posts_url = base_url + "/r/" + subreddit + "/hot.json"
    response = requests.get(posts_url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        hot_list.append(post["data"]["title"])
    if data["data"]["after"] is not None:
        next_subreddit = data["data"]["after"]
        return recurse(next_subreddit)
    else:
        return hot_list


if __name__ == "__main__":
    recurse()
