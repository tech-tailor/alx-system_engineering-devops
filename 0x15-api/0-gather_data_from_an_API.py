#!/usr/bin/python3
"""API script"""

import requests
import sys


def get_username(base_url, id):
    """Get user's name"""
    url = "{}/users/{}".format(base_url, id)
    response = requests.get(url)
    user_dict = response.json()
    get_name = user_dict.get('name')
    return get_name


def get_task(base_url, user_id):
    """Get info about the user's tasks"""
    url = "{}/todos".format(base_url)
    response = requests.get(url)
    task_dict = response.json()
    total_task = 0
    completed_task = 0
    completed_task_title = []
    for task in task_dict:
        if task and task.get("userId") == int(user_id):
            total_task += 1
            if task.get("completed") is True:
                completed_task += 1
                task_title = task.get("title")
                completed_task_title.append(task_title)
    return total_task, completed_task, completed_task_title


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    id = sys.argv[1]

    user_name = get_username(base_url, id)
    total_task, completed_task, task_list = get_task(base_url, id)

    first_line = "Employee {} is done with task({}/{}):"\
        .format(user_name, completed_task, total_task)

    print(first_line)
    for task in task_list:
        print(f"\t{task}")
