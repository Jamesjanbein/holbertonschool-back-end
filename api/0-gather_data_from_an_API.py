#!/usr/bin/python3
"""
Task 0:
Write a Python script that, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":

    # format: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/
    # TOTAL_NUMBER_OF_TASKS):
    # format: tab+space TASK_TITLE
    id = argv[1]
    done_task = 0
    total_task = 0
    todo_list_complete = []

    employee_name = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}')
    employee_todo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')

    for todo in employee_todo.json():
        if todo.get('completed') is True:
            done_task += 1
            total_task += 1
            todo_list_complete.append(todo.get('title'))
        else:
            total_task += 1

    name = employee_name.json()['name']

    print(
        f"Employee {name} is done with tasks({done_task}/{total_task}):")
    for task in todo_list_complete:
        print(f"\t {task}")
