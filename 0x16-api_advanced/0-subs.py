#!/usr/bin/python3
"""
Get total number of subreddit users
"""

import requests


def number_of_subscribers(subreddit):
    base_url = "https://www.reddit.com"
    url = base_url + "/r/" + subreddit + "/about.json"
    print(url)
    response = requests.get(url)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data["data"]["subscribers"]


if __name__ == "__main__":
    number_of_subscribers()
