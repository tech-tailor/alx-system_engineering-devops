#!/usr/bin/python3
"""API script"""

import csv
import requests
import sys


def get_username(base_url, id):
    """Get user's name"""
    url = "{}/users/{}".format(base_url, id)
    response = requests.get(url)
    user_dict = response.json()
    get_name = user_dict['username']
    return get_name


def get_task(base_url, user_id):
    """Get info about the user's tasks"""
    url = "{}/users/{}/todos".format(base_url, user_id)
    response = requests.get(url)
    task_dict = response.json()
    return task_dict


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    id = sys.argv[1]

    user_name = get_username(base_url, id)
    tasks = get_task(base_url, id)

    with open("{}.csv".format(id), 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow(
                [id, user_name, task['completed'], task['title']])
