#!/usr/bin/python3
"""returns information about his/her TODO list progress"""

import json
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
    json_dict = {}
    json_list = []

    # create json file
    file_name = argv[1] + '.json'

    # create a dictionary inside a list
    for data in todo_list:
        user_task = {}
        user_task['task'] = data['title']
        user_task['completed'] = data['completed']
        user_task['username'] = user_list['username']
        json_list.append(user_task)

    # create a list inside a dictionary
    json_dict[argv[1]] = json_list

    # opens json file and write
    with open(file_name, mode='w') as jfile:
        json.dump(json_dict, jfile)
