#!/usr/bin/python3
'''export data in the CSV format.'''
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(
        f'{url}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        dictionary = dict()

        for task in data:
            dictionary[task['userId']] = []

        with open('todo_all_employees.json', 'w',
                  encoding='utf-8') as file:
            for task in data:
                actual_dict = {
                    'username': task['user']['username'],
                    'task': task['title'],
                    'completed': task['completed']
                }
                dictionary[task['userId']].append(actual_dict)
            json.dump(dictionary, file, indent=4)

    else:
        print(f"Error: {response.status_code}")
