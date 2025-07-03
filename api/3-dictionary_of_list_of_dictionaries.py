#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        user_tasks = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)