#!/usr/bin/python3
""" Gather data from an API """

import json
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
        userName = userResponse.json().get('username')

    # Find todos by userId
    params = {'userId': sys.argv[1]}
    getTodosUrl = (
            f'https://jsonplaceholder.typicode.com/todos'
        )
    todosResponse = requests.get(getTodosUrl, params=params)
    todos_data = todosResponse.json()
    filename = f"{sys.argv[1]}.json"
    with open(filename, mode="w") as jsonfile:
        json.dump({sys.argv[1]: [{
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": userName
        } for t in todos_data]}, jsonfile)
