#!/usr/bin/python3
"""Export data in JSON format to file."""
import json
import requests


if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/'
    todos = requests.get(url + 'todos').json()
    users = requests.get(url + 'users').json()
    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        data.update({str(user_id): []})
        for t in (task for task in todos if task.get('userId') == user_id):
            data[str(user_id)].append({"task": t.get('title'),
                                       "completed": t.get('completed'),
                                       "username": username})
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
