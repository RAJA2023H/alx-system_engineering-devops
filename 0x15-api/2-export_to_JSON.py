#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


def fetch_user_todos(user_id):
    """Fetches user and their TODO list based on the user ID."""

    res = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={"userId": user_id}
    )

    user = res.json()
    todos = todo.json()

    return user, todos


def display_todo_progress(user, todos):
    """Displays the TODO list progress for the given user."""
    employee_name = user.get("username")
    all_todos = [todo for todo in todos if todo.get("completed")]
    tasks = []
    for todo in todos:
        tasks.append({
            "USER_ID": user_id,
            "USERNAME": employee_name,
            "TASK_COMPLETED_STATUS": todo.get("completed"),
            "TASK_TITLE": todo.get("title")
            })

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(tasks, jsonfile)


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        user, todos = fetch_user_todos(user_id)
        display_todo_progress(user, todos)
    else:
        print("Usage: ./script.py <employee_id>")
