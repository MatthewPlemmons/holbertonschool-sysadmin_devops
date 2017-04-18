#!/usr/bin/python3
"""Script to return user info based on given ID number"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/users/'
    r_todo = requests.get(url + '{}/todos'.format(argv[1]))
    r_user = requests.get(url + '{}'.format(argv[1]))
    json_todo = r_todo.json()
    fin = [x for x in json_todo if x['completed'] is True]
    print("Employee {} is done with tasks ({}/{}):".format(
        r_user.json().get('name'), len(fin), len(json_todo)))
    for n in fin:
        print("\t{}".format(n.get('title')))
