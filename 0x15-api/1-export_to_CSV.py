#!/usr/bin/python3
"""
Export tasks owned by an employee in CSV format
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    user_id = argv[1]
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
    todo_req = requests.get(todo_url, params=todo_payload)
    todo_json = todo_req.json()
    csvfile = user_id + ".csv"

    for item in todo_json:
        status = item.get('completed')
        title = item.get('title')
        with open(csvfile, "w") as output:
            output.write('"{}","{}","{}","{}"\n'.format
                         (user_id, username, status, title))
