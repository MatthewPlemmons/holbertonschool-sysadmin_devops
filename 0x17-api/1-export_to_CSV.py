#!/usr/bin/python3
"""Export json data to a CSV file."""
from sys import argv
import requests
import csv


if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/users/'
    r_todo = requests.get(url + '{}/todos'.format(argv[1]))
    r_user = requests.get(url + '{}'.format(argv[1]))
    json_todo = r_todo.json()
    username = r_user.json().get('username')
    with open('{}.csv'.format(json_todo[0]['userId']), 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for n in json_todo:
            w.writerow([n.get('userId'), username,
                        n.get('completed'), n.get('title')])