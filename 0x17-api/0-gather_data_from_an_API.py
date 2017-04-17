#!/usr/bin/python3
"""Script to return user info based on given ID number"""

import sys
import requests


if __name__ == "__main__":
    #params = {'completed': 'true'}
    url = ('http://jsonplaceholder.typicode.com/users/{}/todos'.format(
        sys.argv[1]))
    r = requests.get(url)
    #import pdb; pdb.set_trace()
    json_data = r.json()
    
    for todo in json_data:
        print(todo['title'])
