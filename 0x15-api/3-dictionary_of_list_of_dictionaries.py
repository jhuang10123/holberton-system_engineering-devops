#!/usr/bin/python3
"""
Export all tasks by all employees in JSON format
"""
import json
import requests


def get_dict(username, task, status):
    dictionary = {}
    dictionary['username'] = username
    dictionary['task'] = task
    dictionary['completed'] = status
    return dictionary


if __name__ == '__main__':

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    todo_all = requests.get(todo_url)
    todo_all = todo_all.json()

    user_url = 'https://jsonplaceholder.typicode.com/users'
    user_req = requests.get(user_url)
    user_json = user_req.json()

    user_dict = {}
    for item in user_json:
        user_dict[item['id']] = item['username']

    new_dict = {}

    for key in user_dict:
        task_list = []
        for item in todo_all:
            if item['userId'] == key:
                task_list.append(
                    get_dict(
                        user_dict.get(key),
                        item.get('title'),
                        item.get('completed')))
        new_dict[key] = task_list

    filename = "todo_all_employees.json"

    with open(filename, 'w') as output:
        json.dump(new_dict, output)
