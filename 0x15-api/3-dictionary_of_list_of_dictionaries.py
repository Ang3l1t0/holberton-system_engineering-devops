#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    # get url by id:
    user = requests.get('https://jsonplaceholder.typicode.com/users/')
    user_list = user.json()

    json_dict = {}

    for u_name in user_list:
        todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(u_name['id']))
        todo_list = todo.json()

        json_list = []

        # create a new dict with the user items
        for data in todo_list:
            user_task = {}
            user_task["username"] = u_name['username']
            user_task["task"] = data['title']
            user_task["completed"] = data['completed']
            json_list.append(user_task)

        json_dict[u_name['id']] = json_list

    # json file name
    json_file = 'todo_all_employees.json'
    # insert items in file
    with open(json_file, mode='w') as jfile:
        json.dump(json_dict, jfile)
