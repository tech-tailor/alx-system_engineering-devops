#!/usr/bin/python3
"""
Get titles of subreddit top 10 posts
"""

import requests


def top_ten(subreddit):
    """
    Return titles of the first 10 hot posts listed
    """
    base_url = "https://www.reddit.com"
    posts_url = base_url + "/r/" + subreddit + "/hot.json?limit=10"
    response = requests.get(posts_url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)


if __name__ == "__main__":
    top_ten()
