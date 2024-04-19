#!/usr/bin/python3
"""
Task 2:
export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    id = argv[1]

    employee_name = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    employee_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()

    user_name = employee_name['username']
    file_name = f"{id}.json"

    dict_user = {id: []}
    for todo in employee_todos:
        dict_user[id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name
        })

    # user_dict = {
    #     f"{id}.json": [{
    #         "task": task.get("title"),
    #         "completed": task.get("completed"),
    #         "username": user_name
    #     } for task in todo_data]
    # }

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(dict_user, file, indent=4)

    # { "USER_ID": [
    # {
    # "task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS,
    # "username": "USERNAME"
    # }
    # ]
    # }
