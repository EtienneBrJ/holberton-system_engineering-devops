#!/usr/bin/python3
# Script that, using this REST API, for a given employee ID
# returns information about his/her TODO list progress.
import requests
from sys import argv


employeeID = argv[1]
nb_task_done = 0
nb_task_not_done = 0
total_tasks = 0
completed_tasks = []

username = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employeeID)).json().get('name')
todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                    .format(employeeID)).json()

for obj in todo:
    if obj['completed']:
        nb_task_done += 1
        completed_tasks.append(obj['title'])
    else:
        nb_task_not_done += 1

total_tasks = nb_task_not_done + nb_task_done

print("Employee {} is done with tasks({}/{}):".
      format(username, nb_task_done, total_tasks))

for task in completed_tasks:
    print('\t {}'.format(task))
