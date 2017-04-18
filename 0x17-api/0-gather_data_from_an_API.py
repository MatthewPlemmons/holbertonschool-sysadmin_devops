#!/usr/bin/python3
"""Script to return user info based on given ID number"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/users/'
    r_todo = requests.get(url + '{}/todos'.format(sys.argv[1])).json()
    r_user = requests.get(url + '{}'.format(sys.argv[1])).json()
    fin = [x for x in r_todo if x.get('completed') is True]
    print("Employee {} is done with tasks ({}/{}):".format(
        r_user.get('name'), len(fin), len(r_todo)))
    for n in fin:
        print("\t{}".format(n.get('title')))
