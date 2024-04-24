#!/usr/bin/python3
""" Gather data from an API """

import csv
import requests
import sys

if __name__ == '__main__':
    # Find user by employee id
    getUsersUrl = (
        f'https://jsonplaceholder.typicode.com/users/{int(sys.argv[1])}'
    )
    userResponse = requests.get(getUsersUrl)
    if (userResponse.status_code == 200):
        user_data = userResponse.json()
        userName = userResponse.json().get('name')

    # Find todos by userId
    params = {'userId': int(sys.argv[1])}
    getTodosUrl = (
            f'https://jsonplaceholder.typicode.com/todos'
        )
    todosResponse = requests.get(getTodosUrl, params=params)
    todos_data = todosResponse.json()
    result = [{
        "userId": user_data.get('id'),
        "username": user_data.get('name'),
        "status": item["completed"],
        "task_title": item["title"]
    }
    for item in todos_data if item["completed"]
    ]
    filename = f"{user_data.get('id')}.csv"
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for item in result:
            writer.writerow([item["userId"], item["username"], item["status"], item["task_title"]])
    print(f"CSV file '{filename}' has been created successfully.")
