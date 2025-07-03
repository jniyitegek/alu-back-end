#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")
    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    data = {user_id: tasks}
    filename = f"{user_id}.json"
    with open(filename, "w") as f:
        json.dump(data, f)