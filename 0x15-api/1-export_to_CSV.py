#!/usr/bin/python3
"""return information about the employee's todo list progress
by his id"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    api = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(api), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?api={}".
                        format(api), verify=False).json()
    with open("{}.csv".format(api), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(api), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
