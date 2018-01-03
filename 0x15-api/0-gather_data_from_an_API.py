#!/usr/bin/python3
"""
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    user_payload = {'id': argv[1]}
    todo_payload = {'userId': argv[1]}
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    user_url = 'https://jsonplaceholder.typicode.com/users/'

#getting employee info
    user_req = requests.get(user_url, params=user_payload)
    user_json = user_req.json()
#    print("json_response type is:{}".format(type(json_response)))
    for item in user_json:
 #       print(json_response)
 #       print()
        name = item['name']
        # print("Employee {} is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):".format(name))

#getting employee todo
    completed_count = 0
    completed_tasks = []
    total_count = 0
    todo_req = requests.get(todo_url, params=todo_payload)
    todo_json = todo_req.json()
    for item in todo_json:
#        print(type(item.get('completed')))
        total_count += 1
        if item.get('completed'):
            completed_count += 1
            completed_tasks.append(item.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name, completed_count, total_count))
    for item in completed_tasks:
        print("\t" + item)
