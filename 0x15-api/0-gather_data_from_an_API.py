#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import json
    import requests
    import sys

    employeeID = sys.argv[1]
    task_done = 0
    task_ndone = 0
    completed_tasks = []
    usernameR = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employeeID))
    todoR = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(employeeID))

    username = json.loads(usernameR.text)
    todo = json.loads(todoR.text)

    for obj in todo:
        if obj['completed']:
            task_done += 1
        else:
            task_ndone += 1

    print("Employee {} is done with tasks({}/{}):".
          format(username['name'], task_done, task_ndone + task_done))

    for task in todo:
        if task['completed']:
            print("\t {}".format(task['title']))
