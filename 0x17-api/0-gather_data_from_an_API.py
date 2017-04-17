#!/usr/bin/python3
"""Script to return user info based on given ID number"""

import sys
import requests


if __name__ == "__main__":
    r_todo = requests.get('http://jsonplaceholder.typicode.com/users/{}/todos'
                          .format(sys.argv[1]))
    r_user = requests.get('http://jsonplaceholder.typicode.com/users/{}'
                          .format(sys.argv[1]))
    json_todo = r_todo.json()
    fin = [x for x in json_todo if x['completed'] is True]
    employee_name = r_user.json()['name']

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, len(fin), len(json_todo)))
    for n in fin:
        print("\t{}".format(n['title']))
