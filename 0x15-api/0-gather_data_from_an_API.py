#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys

if __name__ == '__main__':
    # Find user by employee id
    getUsersUrl = (
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    )
    userResponse = requests.get(getUsersUrl)
    if (userResponse.status_code == 200):
        user_data = userResponse.json()
        userName = userResponse.json().get('name')

    # Find todos by userId
    params = {'userId': sys.argv[1]}
    getTodosUrl = (
            f'https://jsonplaceholder.typicode.com/todos'
        )
    todosResponse = requests.get(getTodosUrl, params=params)
    todos_data = todosResponse.json()
    completed_counter = sum(1 for t in todos_data if t['completed'])
    print("Employee {} is done with tasks({}/{}):".format(userName, completed_counter, len(todos_data)))
    for t in todos_data:
        if t['completed']:
            print(f'\t {t["title"]}')
