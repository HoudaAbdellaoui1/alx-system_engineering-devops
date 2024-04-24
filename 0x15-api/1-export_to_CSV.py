#!/usr/bin/python3
""" Gather data from an API """

import csv
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
    filename = f"{sys.argv[1]}.csv"
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for item in result:
            writer.writerow([item["userId"], item["username"],
                             item["status"], item["task_title"]])
