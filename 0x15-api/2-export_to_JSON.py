#!/usr/bin/python3
""" Gather data from an API """

import csv
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
    result = [{
        "userId": sys.argv[1],
        "username": userName,
        "status": item["completed"],
        "task_title": item["title"]
        }
        for item in todos_data
    ]
    formatted_data = {sys.argv[1]: [
        {"task": item["task_title"], "completed": item["status"],
            "username": userName}
        for item in result
    ]}
    formatted_json = json.dumps(formatted_data, ensure_ascii=False)
    filename = f"{sys.argv[1]}.json"
    with open(filename, "w") as outfile:
        outfile.write(formatted_json)
