#!/usr/bin/python3
"""
Task 1:
export data in the CSV format.
"""

import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]

    employee_name = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}')
    employee_todo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')

    name = employee_name.json()['username']
    file_name = f"{id}.csv"
    with open(file_name, "w", encoding="utf-8") as file:
        for todo in employee_todo.json():
            completed_status = todo.get('completed')
            task_title = todo.get('title')
            file.write(
                f'"{id}","{name}","{completed_status}","{task_title}"\n')
    # format "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
    # "TASK_TITLE" in USER_ID.csv
