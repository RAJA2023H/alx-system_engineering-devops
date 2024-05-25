#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""
import json
import requests


def main():
    """Main function to gather data and write to JSON file."""
    # Fetch all users
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    # Fetch all todos
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos_response.json()

    all_tasks = {}

    # Iterate through users
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = []
        # Iterate through todos to find tasks for current user
        for todo in todos:
            if todo.get("userId") == user_id:
                user_tasks.append({
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })
        all_tasks[str(user_id)] = user_tasks

    # Write data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    main()
