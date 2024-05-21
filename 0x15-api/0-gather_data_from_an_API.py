#!/usr/bin/python3
"""
Python script that uses the REST API at https://jsonplaceholder.typicode.com/
to retrieve and display information about an employee's TODO list progress
based on the given employee ID.
"""
import requests
import sys

def fetch_user_todos(user_id):
    """Fetches user and their TODO list based on the user ID."""
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": user_id})

    user = user_response.json()
    todos = todos_response.json()

    return user, todos

def display_todo_progress(user, todos):
    """Displays the TODO list progress for the given user."""
    completed_todos = [todo for todo in todos if todo.get("completed")]

    print(f"Employee {user.get('name')} is done with tasks({len(completed_todos)}/{len(todos)}):")

    for todo in completed_todos:
        print(f"\t {todo.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        user, todos = fetch_user_todos(user_id)
        display_todo_progress(user, todos)
    else:
        print("Usage: ./script.py <employee_id>")
