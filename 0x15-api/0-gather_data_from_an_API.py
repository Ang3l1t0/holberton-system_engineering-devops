#!/usr/bin/python3
"""returns information about his/her TODO list progress"""

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

    # declare task counters
    total_task = 0
    done_task = 0
    list_task = []

    # take values
    for task in todo_list:
        if task['completed'] is True:
            done_task += 1
            list_task.append(task['title'])
        total_task += 1

    # print output
    print(
        'Employee {} is done with tasks({}/{}):'
        .format(user_list['name'], done_task, total_task), end='\n\t ')
    print(*list_task, sep='\n\t ')
