#!/usr/bin/python3
"""Export json data to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/users/'
    r_todo = requests.get(url + '{}/todos'.format(sys.argv[1])).json()
    r_user = requests.get(url + '{}'.format(sys.argv[1])).json()
    username = r_user.get('username')
    with open('{}.csv'.format(r_user.get('id')), 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for n in r_todo:
            w.writerow([n.get('userId'), username,
                        n.get('completed'), n.get('title')])
