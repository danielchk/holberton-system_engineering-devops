#!/usr/bin/python3
"""return to-do list with the employee ID"""
import json
import requests
import sys

if __name__ == "__main__":
    userid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userid)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": userid}).json()

    with open("{}.json".format(userid), "w") as jsonfile:
        json.dump({userid: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
