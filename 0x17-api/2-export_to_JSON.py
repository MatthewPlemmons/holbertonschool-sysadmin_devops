#!/usr/bin/python3
"""Export data in JSON format to file."""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/users/'
    r_todo = requests.get(url + '{}/todos'.format(sys.argv[1])).json()
    r_user = requests.get(url + '{}'.format(sys.argv[1])).json()
    user_id = r_user.get('id')
    username = r_user.get('username')
    data = {str(user_id): []}
    for n in r_todo:
        data[str(user_id)].append({"task": n.get('title'),
                                   "completed": n.get('completed'),
                                   "username": username})
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(data, f)
