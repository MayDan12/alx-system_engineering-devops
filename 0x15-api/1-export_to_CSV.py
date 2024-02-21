#!/usr/bin/python3
""" This python script Export api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    response = requests.get(url_user)
    
    user_name = response.json().get('username')
    task = url_user + '/todos'
    response = requests.get(task)
    tasks = response.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """This gets the Completed tasks"""
            title_task = task.get('title')
            """This gets the titles of the task"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))