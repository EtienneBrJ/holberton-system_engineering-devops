#!/usr/bin/python3
# Script that, using this REST API, for a given employee ID
# returns information about his/her TODO list progress.
import requests
import json
from sys import argv


employeeID = argv[1]

if __name__ == "__main__":
    username = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employeeID)).json().get('name')
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(employeeID)).json()

    with open("{}.json".format(employeeID), "w") as jsonfile:
        json.dump({employeeID: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todo]}, jsonfile)
