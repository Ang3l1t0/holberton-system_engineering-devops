#!/usr/bin/python3
"""returns information about his/her TODO list progress"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    # get url by id
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))

    # convert to json
    user_list = user.json()
    todo_list = todo.json()

    # create csv file
    file_name = argv[1] + '.csv'

    # opens csv file and write
    with open(file_name, mode='w') as f:
        user_data = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for data in todo_list:
            user_data.writerow([data['userId'], user_list['username'],
                                data['completed'], data['title']])
