#!/usr/bin/python3
"""Script to export data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # get url by id
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/')

    # convert to json
    user_list = user.json()
    json_dict = {}
    json_list = []

    for u_name in user_list:
        todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(u_name['id']))
        todo_list = todo.json()

        # create a dictionary inside a list
        for data in todo_list:
            user_task = {}
            user_task["task"] = data['title']
            user_task["completed"] = data['completed']
            user_task["username"] = u_name['username']
            json_list.append(user_task)

        # create a list inside dictionary
        json_dict[u_name['id']] = json_list

    # create json file
    json_file = 'todo_all_employees.json'

    # open json file and write
    with open(json_file, mode='w') as jfile:
        json.dump(json_dict, jfile)
