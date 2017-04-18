#!/usr/bin/python3
"""Export json data to a CSV file."""

import sys
import requests
import csv


if __name__ == "__main__":
    r_todo = requests.get('http://jsonplaceholder.typicode.com/users/{}/todos'
                          .format(sys.argv[1]))
    r_user = requests.get('http://jsonplaceholder.typicode.com/users/{}'
                          .format(sys.argv[1]))
    json_todo = r_todo.json()
    username = r_user.json()['username']
    with open('{}.csv'.format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for n in json_todo:
            data = [n['userId'], username, n['completed'], n['title']]
            writer.writerow(data)
