#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""

if __name__ == "__main__":

    import requests
    import sys

    employeeID = sys.argv[1]
    task_done = 0
    task_ndone = 0
    completed_tasks = []
    username = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employeeID)).json().get('name')
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(employeeID)).json()

    for obj in todo:
        if obj['completed']:
            task_done += 1

        else:
            task_ndone += 1

    print("Employee {} is done with tasks({}/{}):".
          format(username, task_done, task_ndone + task_done))

    for task in todo:
        if task['completed']:
            print("\t {}".format(task['title']))
