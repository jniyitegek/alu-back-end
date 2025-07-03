#!/usr/bin/python3
"""
Module to gather data from an API and display employee TODO progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    user_resp = requests.get(user_url)
    todos_resp = requests.get(todos_url)

    if user_resp.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user = user_resp.json()
    todos = todos_resp.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    num_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))