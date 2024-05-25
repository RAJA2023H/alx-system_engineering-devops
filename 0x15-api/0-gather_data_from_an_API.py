#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""


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

    employee_name = user.get("name")
    all_todos = [todo for todo in todos if todo.get("completed")]

    print(
            "Employee {} is done with tasks({}/{}):".format(
                employee_name, len(all_todos), len(todos)
            )
    )

    for todo in all_todos:
        print(f"\t {todo.get('title')}")


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1].isdigit():i
        user_id = sys.argv[1]
        user, todos = fetch_user_todos(user_id)
        display_todo_progress(user, todos)
    else:
        print("Usage: ./script.py <employee_id>")
