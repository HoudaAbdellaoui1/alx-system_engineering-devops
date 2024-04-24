#!/usr/bin/python3
""" Gather data from an API """

import json
import requests
import sys

if __name__ == '__main__':
    # Find user by employee id
    # getUsersUrl = (
    #     f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    # )
    # userResponse = requests.get(getUsersUrl)
    # if (userResponse.status_code == 200):
    #     user_data = userResponse.json()
    #     userName = userResponse.json().get('username')

    # Find todos by userId
    # params = {'userId': sys.argv[1]}
    getUsersUrl = (
        f'https://jsonplaceholder.typicode.com/users'
    )
    response_users = requests.get(getUsersUrl)
    users = {user['id']: user['username'] for user in response_users.json()}
    
    getTodosUrl = (
            f'https://jsonplaceholder.typicode.com/todos'
        )
    todosResponse = requests.get(getTodosUrl)
    todos_data = todosResponse.json()
    formatted_data = {}

    for todo in todos_data:
        user_id = todo['userId']
        task_title = todo['title']
        completed = todo['completed']
        username = users.get(user_id, {user_id})

        if user_id not in formatted_data:
            formatted_data[user_id] = []
        
        formatted_data[user_id].append({
            "username": username,
            "task": task_title,
            "completed": completed
        })
    filename = "todo_all_employees.json"
    with open(filename, mode="w") as jsonfile:
        json.dump(formatted_data, jsonfile, indent=4)
