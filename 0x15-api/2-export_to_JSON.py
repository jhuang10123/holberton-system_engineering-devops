#!/usr/bin/python3
"""
Export tasks owned by an employee in JSON format
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    user_payload = {'id': argv[1]}
    todo_payload = {'userId': argv[1]}
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users'

# getting employee data
    user_req = requests.get(user_url, params=user_payload)
    user_json = user_req.json()
    for item in user_json:
        username = item['username']

# getting employee todo
    filename = argv[1] + ".json"
    to_dict = {}
    json_dict = {}
    val_list = []
    todo_req = requests.get(todo_url, params=todo_payload)
    todo_json = todo_req.json()
    for item in todo_json:
        status = item.get('completed')
        title = item.get('title')
        to_dict.update(
            {"task": title, "completed": status, "username": username})
        val_list.append(to_dict)
        json_dict = {argv[1]: val_list}

        with open(filename, 'w') as output:
            json.dump(json_dict, output)
