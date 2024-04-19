#!/usr/bin/python3
"""
Task 3:
export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":

    employee_users = requests.get(
        f'https://jsonplaceholder.typicode.com/users').json()
    employee_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos').json()

    dict_user = {}
    file_name = "todo_all_employees.json"

    for user in employee_users:
        id = user.get("id")
        dict_user[id] = []
        for todo in employee_todos:
            if user.get('id') == todo.get('userId'):
                dict_user[id].append({
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })
    # for user in employee_users:
    #     dict_user = []
    #     username = user.get('username')
    #     for task in employee_todos:
    #         if user.get('id') == task.get('userId'):
    #             dict_user

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(dict_user, file, indent=4)

    # { "USER_ID":
    # [{
    # "username": "USERNAME",
    # "task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS
    # }]
    # , "USER_ID":
    # [ {"username": "USERNAME",
    # "task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS},
    # ]}
